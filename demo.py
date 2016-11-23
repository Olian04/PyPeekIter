from peekiter import PeekIter

# Using a while loop
foo = PeekIter(i for i in range(10))
while foo:
    print(foo.next, foo.peek)

# Using a for loop
foo = PeekIter(i for i in range(10))
for _next in foo:
    print(_next, foo.peek)


# Using recursion
foo = PeekIter(i for i in range(10))
def bar():
    print(foo.next, foo.peek)
    if foo:
        bar()
bar()
