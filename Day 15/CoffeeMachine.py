from main import MENU, resources


def check_resources(target_drink, remained_water, remained_milk, remained_coffee):
    sufficient = True
    if MENU[target_drink]["ingredients"]["water"] > remained_water:
        sufficient = False
        lack = "water"
    if MENU[target_drink]["ingredients"]["coffee"] > remained_coffee:
        sufficient = False
        lack = "coffee"
    if target_drink != "espresso":
        if MENU[target_drink]["ingredients"]["milk"] > remained_milk:
            sufficient = False
            lack = "milk"
    if not sufficient:
        print(f"Sorry there's not enough {lack}.")
    return sufficient


def process_money(target_drink):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    drink_price = MENU[target_drink]["cost"]
    total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    if total >= drink_price:
        charge = total - drink_price
        if charge != 0:
            print(f"Here is ${round(charge,2)} in charge")
        sufficient = True
    else:
        print("Sorry that's not enough money. Money refunded")
        sufficient = False
    return sufficient


def make_coffee(target_drink, remained_water, remained_milk, remained_coffee):
    remained_water = remained_water - MENU[target_drink]["ingredients"]["water"]
    remained_coffee = remained_coffee - MENU[target_drink]["ingredients"]["coffee"]
    if target_drink != "espresso":
        remained_milk = remained_milk - MENU[target_drink]["ingredients"]["milk"]
    return remained_water, remained_milk, remained_coffee


def report(remained_water, remained_milk, remained_coffee, total_money):
    print(f"Water: {remained_water}ml")
    print(f"Milk: {remained_milk}ml")
    print(f"Water: {remained_coffee}g")
    print(f"Money: ${total_money}")


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
turn = "on"
money = 0
while turn == "on":
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        break
    elif drink == "report":
        report(water, milk, coffee, money)
        continue
    elif not check_resources(drink, water, milk, coffee):
        continue
    else:
        print("Please insert coin")
        operation = process_money(drink)
        if operation:
            print(f"Here is your {drink} ☕. Enjoy!")
            water, milk, coffee = make_coffee(drink, water, milk, coffee)
            money = money + MENU[drink]["cost"]
