class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = { # Every coffeemaker objects starts with default resources, which are this much.
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self): # Prints current report of this object.
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink): # Checks if to make the said drink, this object has sufficient resources
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order): # makes required coffee and edits it resources.
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:  # order is an object of MenuItem , thus has an attribute ingredients and
            # attributes are accessed with '.' .
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
