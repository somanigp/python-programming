MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def check_if_enough_money(user_selection):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies? :"))
    total_amt = (pennies*0.01) + (nickles*0.05) + (dimes*0.10) + (quarters*0.25)
    return round(total_amt - MENU[user_selection]["cost"], 2)


def check_if_report(user_selection,resources):
    coffee_available = resources["coffee"] - MENU[user_selection]["ingredients"]["coffee"]
    water_available =  resources["water"] - MENU[user_selection]["ingredients"]["water"]
    if user_selection == "latte" or user_selection == "cappuccino":
        milk_available = resources["milk"] - MENU[user_selection]["ingredients"]["milk"]
        return [coffee_available, water_available, milk_available]
    return [coffee_available, water_available, 1000 ]


money = 0
machine_on = True
resources = {
    "coffee": 100,
    "water": 300,
    "milk": 200,
}

while machine_on:
    ingredients = []
    user_selection = input("What would you like? (espresso/latte/cappuccino): \n").lower()
    # TODO : Print Report # IDE Feature
    if user_selection == "report":
        for i,j in resources.items():
            print(f"{i}: {j}")
        print(f"Money : ${money}")
    # TODO : Check resource sufficient
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        ingredients = check_if_report(user_selection,resources)
        if (ingredients[0] >= 0) and (ingredients[1] >= 0) and (ingredients[2] >= 0) :
            amt_left = check_if_enough_money(user_selection)
            if amt_left < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if amt_left > 0:
                    print(f"Here is ${amt_left} in change.")
                print(f"Here is your {user_selection} ☕️. Enjoy!")
                money += MENU[user_selection]["cost"]
                resources["coffee"] = ingredients[0]
                resources["water"] = ingredients[1]
                if ingredients[2] < 1000:
                    resources["milk"] = ingredients[2]
        else:
            list_of_insufficient_items = []
            for i in range(3):
                if i == 0 and ingredients[i] < 0:
                    list_of_insufficient_items.append("coffee")
                if i == 1 and ingredients[i] < 0:
                    list_of_insufficient_items.append("water")
                if i == 2 and ingredients[i] < 0:
                    list_of_insufficient_items.append("milk")
            print("Sorry there is not enough ", ",".join(list_of_insufficient_items))
    elif user_selection == "no":
        print("Thanks for coming")
        machine_on = False
    else:
        print("Invalid Input")




