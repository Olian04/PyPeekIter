# What is PeekIter
[PeekIter](https://pypi.python.org/pypi/peekiter) is a __Python3__ package that implements peeking into iterators via a wrapper class.
Peeking means looking at the next element from a generator without consuming it.

# Install

```
pip install peekiter
```

# How to use it
[Live Demo v0.1](https://repl.it/E6UU/2)

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
