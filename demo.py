from peekiter import PeekIter, __VERSION
print("Demoing PeekIter version: " + __VERSION)

print("\nUsing a while loop")
foo = PeekIter(i for i in range(10))
while foo:
    print("Next: {}\t\tPeek: {}".format(foo.next, foo.peek))


print("\nUsing a for loop")
foo = PeekIter(i for i in range(10))
for _next in foo:
    print("Next: {}\t\tPeek: {}".format(_next, foo.peek))


print("\nUsing recursion")
foo = PeekIter(i for i in range(10))
def bar():
    print("Next: {}\t\tPeek: {}".format(foo.next, foo.peek))
    if foo:
        bar()
bar()


print("\nUsing custom terminals")
foo = PeekIter((i for i in range(10)), terminal=4)
while foo:
    print("Next:", foo.next) # 0, 1, 2, 3 (terminal is exclusive)
print("Next:", foo.next) # 4 (any further calls will produce the terminal)
print("Peek:", foo.peek) # 4 (works with peek as well, ofc)
