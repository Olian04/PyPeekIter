# What is PeekIter
[PeekIter](https://pypi.python.org/pypi/peekiter) is a __Python3__ package that implements peeking into iterators via a wrapper class.
Peeking means looking at the next element from a generator without consuming it.

# How to use it

### While
```python
# Using a while loop
foo = PeekIter(i for i in range(10))
while foo:
    print(foo.next, foo.peek)
```
### For

```python
# Using a for loop
foo = PeekIter(i for i in range(10))
for _next in foo:
    print(_next, foo.peek)
```
### Recursion

```python
# Using recursion
foo = PeekIter(i for i in range(10))
def bar():
    print(foo.next, foo.peek)
    if foo:
        bar()
bar()
```

# Planed

* Add custom terminals.
    * v0.1 uses a hardcoded `None` terminal.
