from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
on = True
while on:
    user = input(f"What would you like?({menu.get_items()})").lower()
    if user == "off":
        on = False
    elif user == "report":
        coffee_report = coffee_maker.report()
        money_report = money_machine.report()
    else:
        drink = menu.find_drink(user)
        sufficient_resources = coffee_maker.is_resource_sufficient(drink)
        if sufficient_resources:
            sufficient_payment = money_machine.make_payment(drink.cost)
            if sufficient_payment:
                coffee_maker.make_coffee(drink)









