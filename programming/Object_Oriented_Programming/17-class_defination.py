# Class Declaration
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

    def follow(self, user):  # Argument 'user' will be an 'User' object**.
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


