from machine_data import MENU,resources

money = 0.0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25 +
             dimes * 0.10 +
             nickles * 0.05 +
             pennies * 0.01)
    return round(total, 2)


def make_coffee(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    print(f"Here is your {drink}. Enjoy!\n")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins()
            cost = MENU[choice]["cost"]

            if payment < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                money += cost
                make_coffee(choice)
    else:
        print("Invalid choice. Please try again.")
