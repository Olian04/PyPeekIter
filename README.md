[![Downloads](https://pepy.tech/badge/peekiter)](https://pepy.tech/project/peekiter) [![Downloads](https://pepy.tech/badge/peekiter/month)](https://pepy.tech/project/peekiter)

# What is PeekIter
[PeekIter](https://pypi.python.org/pypi/peekiter) is a __Python3__ package that implements peeking into iterators via a wrapper class.
Peeking means looking at the next element from a generator without consuming it.

# Install

```
sudo pip3 install peekiter
```

# How to use it
[Live Demo v1.1](https://repl.it/E6UU/15)

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

### Custom terminal

```python
foo = PeekIter((i for i in range(10)), terminal=4)
while foo:
    print(foo.next) # 0, 1, 2, 3 (terminal is exclusive)
print(foo.next) # 4 (any further calls will produce the terminal)
print(foo.peek) # 4 (works with peek as well, ofc)
```

# Version History

## 1.1
* Now featuring custom `terminals`.

## 1.0
* Works in `While` loops
* Works in `For` loops
* Works in `Recursive` calls
