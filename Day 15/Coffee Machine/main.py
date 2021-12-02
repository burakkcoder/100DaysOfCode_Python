import time
from menu import MENU, resources, profit

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def is_enough_coins(coins,drink_cost):
    if coins > drink_cost:
        change = round(coins - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_drink(name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name} ☕. Enjoy!")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Turning off...")
        time.sleep(2)
        print("Turned Off")
        break
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coins()
            if is_enough_coins(payment,drink["cost"]):
                make_drink(choice,drink["ingredients"])


