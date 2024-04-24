from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()


cafe_maker = CoffeeMaker()
check_out = MoneyMachine()
is_on = True
while is_on:
    option = MENU.get_items()
    choice = input(f"What would you  like? ({option}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cafe_maker.report()
        check_out.report()
    else:
        drink = MENU.find_drink(choice)
        if cafe_maker.is_resource_sufficient(drink) and check_out.make_payment(drink.cost):
            cafe_maker.make_coffee(drink)





