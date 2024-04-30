# Dynamic Typing : Change a variable data type by changing content of that variable.
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
a = 2
print(a, type(a))
a = "two"
print(a, type(a))

# Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type
# This works because the variable does not have a type; it can name any object. After bob=1, you'll find that type(bob)
# returns int, but after bob="bob", it returns str. (Note that type is a regular function, so it evaluates its argument,
# then returns the type of the value.)
