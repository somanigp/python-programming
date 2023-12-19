from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# NOTE :  All 3 Objects are created here with their attributes set here, all the changes done to these 3 objects can
# change the attributes of these objects in while loop. Thus these objects data will keep changing. If we create another
# CoffeeMaker it will have resources of its own and we can change those resources and it wont affect below coffeeMaker.

# Object created and stored in these variables
menu_created = Menu()  # Created a menu object , The constructor during initialization only puts 3 objects of MenuItem
# in the Menu Object created. Thus our Menu object menu_created has 3 MenuItems already.
coffee_maker_created = CoffeeMaker()  # created a object of CoffeeMaker class. # we can name the variable money_machine
# also which is the name of module we imported
money_machine_created = MoneyMachine()  # created a object of MoneyMachine class

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu_created.get_items()}): ").lower()  # object menu_created method to get
    # all the items in the menu object.
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_created.report()  # We created a new coffee maker at top and this is its( this objects
        # 'coffee_maker_created') current report. Current amt of resources in this machine.
        money_machine_created.report()  # This is a report for object 'coffee_maker_created' only which we created at
        # start. The current amt of money in this machine
    else:
        drink = menu_created.find_drink(choice)  # returns an object of MenuItem class, which has name, cost and
        # ingredients. Basically functions creates a new object of MenuItem Class for 'choice' option and returns that.
        if coffee_maker_created.is_resource_sufficient(drink):  # check with our Object coffee_maker_created, if **this
            # object has enough resources to make the user's coffee.
            if money_machine_created.make_payment(drink.cost):  # Object money_machine_created provides
                # functionality to process payment and check if payment is enough both in this function. Its input is
                # cost of the desired drink in menu. 'drink' is a MenuItem Object for 'choice' , so we can access its
                # attribute like this.
                coffee_maker_created.make_coffee(drink)  # Use Object coffee_maker_created to create Coffee

# Flow Chart ->
# 1. Create a Menu ( With Menu Object ) , Coffee Maker (With CoffeeMaker Class ) and a MoneyMachine
# ( with MoneyMachine class )
# 2. Take User Input about which drink it wants
# 3. Find and get all info about the drink selected by user from our Menu Object menu_created.
# 4. Check in our Object coffee_maker_created if **this object has capacity/resources to make the desired drink
# 5. If it has then check then process the user payment and get the total amt user paid
# 6. Check if the amt paid is sufficient and if it is then call the coffee_maker_created object to create coffee for
# User


