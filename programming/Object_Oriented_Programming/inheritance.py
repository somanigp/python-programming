class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("inhale, exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()  # super() - call to the super class. Inherit all attributes and methods of superclass

    def breath(self):  # Overriding a method in super/parent class
        # Way to call a method of superclass
        super().breath()  # First calling all the functions of superclass and then adding onto it. This can be skipped.
        print("Under Water")

    def move(self):
        print(self.num_of_eyes)  # Accessing an attribute from superclass.
        print("Swimming in water")


nemo = Fish()
nemo.move()
print(nemo.num_of_eyes)
nemo.breath()

# Fish.move() - error as move has self in it.
# Inheritance: Take an existing class that we or someone else created and build on top of it.
# If a function takes a specific class (Animal) as input, then we can also pass its subclass (Fish) as input as they
# share the same attributes and methods. So all the use cases of it are valid. NOTE: vice versa is not true
