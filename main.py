from resources import MENU
from resources import resources

machine_on = True


def print_resources(money):
    print(f"Water: {resources["water"]}ml\n"
          f"Coffee: {resources["coffee"]}g\n"
          f"Milk: {resources["milk"]}ml\n"
          f"Money: ${money}")


def process_order(drink, money):
    order_ingredients = MENU[drink]["ingredients"]
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}.")
            return money

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if total_coins < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return money
    else:
        change = round((total_coins - MENU[drink]["cost"]), 2)
        print(f"Here is ${change} in change.")
        resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
        if drink == "latte" or drink == "cappuccino":
            resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
        print(f"Here is your {drink}. Enjoy!")
        money = money + MENU[drink]["cost"]
        return money


def coffee_machine(status):
    money_in_machine = 0
    while status:
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink_choice == "espresso" or drink_choice == "latte" or drink_choice == "cappuccino":
            money_in_machine = process_order(drink_choice, money_in_machine)
        elif drink_choice == "report":
            print_resources(money_in_machine)
        elif drink_choice == "off":
            status = False
            return status
        else:
            print("Invalid option")


coffee_machine(machine_on)
