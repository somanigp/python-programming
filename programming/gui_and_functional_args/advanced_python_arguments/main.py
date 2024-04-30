# advanced python args to specify wider range of inputs

# Keyword args
def func(a,b,c) -> None:
    pass
func(a=1, b=2, c=3)

# Functions with default values
def func1(a:int =1, b:int =2, c: int =3) -> None:
    pass
func1(b=5) # func1(a=1, b=5, c=3)

# Unlimited Positional Arguments : Function that can take any num of args, position matters
# * - means the function can have any number of arguments
def func3(*args):  # args - arguments, its just a variable and can be any name
    print(args[0]) # Its a tuple and thus indexed.
    for i in args:  # loop through the arguments which are in form of tuple
        print(i)

def add(*args: int) -> int:  # :int means args are expected of type int
    sum_is = 0
    for i in args:
        sum_is += i
    return sum_is

print(add(1,2))
print(add(1,2,3,4,5))

# **kwargs : Many Keyworded Arguments

def calculate(n, **kwargs):
    print(kwargs)  # Its a dictionary - {'add': 3, 'multiply': 5}
    if "add" in kwargs:
        n += kwargs["add"]
    if kwargs.get("multiply") is not None:
        n *= kwargs["multiply"]
    print(n)

calculate(1, add=3, multiply=5)
calculate(1, add=3)

# Valid dict (key values)
dict1 = {1: 'one', 2.0: 'two', 'three': 3}


class Person:
    def __init__(self, **kw):
        self.name = kw.get("name")  # Returns None is key doesn't exists
        self.age = kw.get("age")


person = Person(name="John", age=36)
print(person.name)



def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64) # 4, (7, 3, 0), {'x': 10, 'y': 64}

