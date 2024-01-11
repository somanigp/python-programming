# Class Declaration
# NOTE: **
from Classes.coffee_machine.coffee_maker import CoffeeMaker  # '.' to navigate when doing imports in .py file
# from ..higher_or_lower.art import logo  # Cant do this as relative imports are only within packages. To
# import like this we need to change our project structure into packages.


class User:  # 'class' Keyword and name in PascalCase. All Class details go inside this indented
    # pass  # when you want to skip writing code from now.

    # Constructor : What should happen when our object is created. Like creating attributes and assigning it values
    # during initial construction(Initialization),etc.
    # Also known as initializing an object when an object is created with class constructor. Where variables, counters
    # and switches, etc. are set.
    def __init__(self, user_id, username):  # this is a special constructor, init function. This is called each time a object is
        # created using this** constructor. It can have parameter requirements too.
        # Initialise Attributes
        print("New User Created")
        self.id = user_id  # id - variable associated with the object
        self.username = username  # self - represents actual object being created. self represents object itself.
        self.followers = 0  # Attributes which will have some default initial values which can be later changed for
        # that object. user1.followers will be 0 when user1 is created.
        self.following = 0

    # Creating Methods for a class - things it does ( functions ).
    # NOTE : Function attached to an 'object' is Method.
    def add_follower(self):  # Self is the first parameter, and it is not an argument needed by user to give.
        self.followers += 1

    def follow(self, user: "User"):  # Argument 'user' will be an 'User' object**.
        user.followers += 1
        self.following += 1


# user1 = User()
# user1.id = "001"  # not preferred way as their can be errors as well as too tedious.
# user1.username = "somanigp"
# user1.password = "qwerty123"  # NOTE : We can add attributes (which are basically variables associated with an 'object')
# # to an object. We can add more attributed then defined during object initiation. Any number of variables can be attached
# # to an object after its creation and those can be altered and used accordingly.
# print(user1.username)  # using created attributes
#
# user2 = User()
# print(user2.password) # Attributes created like this , individually on objects are associated with objects.

# NOTE: For classes PascalCase and everything else snake_case in Python.

# NOTE : compulsory to pass 2 parameters during initialization as its needed by constructor
user_1 = User("001", "somanigp")  # Initialization / Initializing an object.
print(user_1.username)
user_1.followers += 1
print(user_1.followers)  # Changing Attributes of an 'object'
user_1.add_follower()
print(user_1.followers)

user_2 = User("002","raksha")

user_2.follow(user_1)  # Increases user_2 followers count by 1 and this objects user_2 following by 1
print(user_1.followers)
print(user_2.following)


# NOTE : In Python, a class cannot have multiple constructors in the same way as some other programming languages (like Java or C++) where method overloading allows different constructors to have different signatures.

# class MyClass:
#     def __init__(self, param1=None, param2=None):  # If passing a value as argument this(param1=None) gets overriden.
#         if param1 is None and param2 is None:
#             # Default initialization
#             self.param1 = 0
#             self.param2 = 0
#         else:
#             # Custom initialization
#             self.param1 = param1
#             self.param2 = param2

# # Creating objects with different initialization options
# obj1 = MyClass()  # Initializes with default values (0, 0)
# obj2 = MyClass(10)  # Initializes with param1=10 and param2=None
# obj3 = MyClass(20, 30)  # Initializes with param1=20 and param2=30

# # Accessing object attributes
# print(obj1.param1, obj1.param2)  # Output: 0 0
# print(obj2.param1, obj2.param2)  # Output: 10 0
# print(obj3.param1, obj3.param2)  # Output: 20 30


# NOTE: When it shows (self,distance) -> it means it only takes one argument i.e. distance.
# NOTE: When it shows (self) -> No argument needed

# **** NOTE ****
# You can change attributes of an object through methods inside a function like func1, but not directly change
# attribute inside a function which is not object's method.

# class Demo:
#   def __init__(self):
#     self.x = 10


# demo = Demo()
# print(demo.x)

# def func1():
#   demo.x = 20  # does change the attribute

# func1()
# print(demo.x) # prints 20
# demo.x = 30
# print(demo.x) # 30


# NOTE:
# class Demo:
#
#   class_variable = 10  # Class variable
#
#   def __init__(self, param1 = 0, param2 = 0):  # Setting default values if None passed
#     self.x = param1
#     self.y = param2

#   def x_is(self):  # self - object method , and not class
#     return self.x

#   def hello(self):
#     print("hello" + self.class_variable)  # using class_variable.

#   def hello_2():
#     print("hello2")

#   def own_input(self, demo_item: 'Demo'):  # demo_item parameter should only take input which is of the same class ie demo. NOTE : '' not needed when there is any other class as requirement.
#     return demo_item.x

# demo1 = Demo()
# print(demo1.x)
# print(demo1.y)
# print(demo1.x_is())
# # Demo.x_is() - error
# demo1.hello()
# # Demo.hello() - error
# Demo.hello_2() # Works , method of class
# Demo.class_variable # Works , class variable

# demo2 = Demo(9)
# print(demo2.x)
# print(demo2.y)

# demo3 = Demo(8,9)
# print(demo3.x)
# print(demo3.y)

# # O/P:
# # 0
# # 0
# # 9
# # 0
# # 8
# # 9
