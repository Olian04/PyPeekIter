"""
[PeekIter]: Wrapper class for iterators, implements peeking.
"""
__VERSION = "0.1"
__AUTHOR = "Olian04"

class PeekIter:
    """PeekIter wrapper class, adds peek, done and next functionality to an iter.

    [iterator]: The iterator to wrap.
        - In v0.1 the iterator may NOT produce None results.
          None is used internaly to signal end of data.
    """
    def __init__(self, iterator):
        self._iter = iter(iterator)
        self._peeked = None

    def __repr__(self):
        return "PeekIter(done={done}, next='{next}', inner='{inner}')".format(
                next=self.peek,
                done=self.done,
                inner=type(self._iter))

    def __bool__(self):
        "Returns True while there are more elements available from the generator"
        return not self.done

    def __next__(self):
        return self.next

    def __iter__(self):
        "Yields every element in the iterator, then raises StopIteration."
        while not self.done:
            yield self.next
        raise StopIteration

    @property
    def next(self):
        "Get the next value from the generator."
        if self._peeked != None:
            val, self._peeked = self._peeked, None
            return val
        return self._try_next()

    @property
    def peek(self):
        "Peek at the next value from the generator."
        if self._peeked != None:
            return self._peeked
        self._peeked = self._try_next()
        return self._peeked

    @property
    def done(self):
        "Returns true if the next value in the iterator is equal to the terminal_token."
        return self.peek == None

    def _try_next(self):
        "Returns the next item from the iterator or, if that fails, returns the terminal_token."
        try:
            return next(self._iter)
        except StopIteration:
            return None

    def fork(self):
        """Forks the generator as is, i.e. in its current state.

        [WARNING]: This utelizes itertools.tee, which makes PeekIter.fork() a highly demanding operation.
        Do NOT use this operation unless absolutely nessessary.
        [WARNING]: Iterator has to be finit as of the time of the fork.
            [NOT FINIT, DUE TO INFINIT LOOP "while (true)"]:
                i = 0
                while (true):
                    yield i
                    i += 1
            [MIGHT NOT BE FINIT, DUE TO OUTER DEPENDENCY "run"]:
                i = 0
                while (run):
                    yield i
                    i += 1

        """
        from itertools import tee
        _iters = tee(self._iter)
        self._iter = _iters[0]
        ret = PeekIter(_iters[1])
        ret._peeked = self._peeked
        return ret


if __name__ == '__main__':
    pi1 = PeekIter([1,2,3,4,5,6,7])
    print(pi1.peek)
    pi2 = pi1.fork()
    print(pi2.peek)
