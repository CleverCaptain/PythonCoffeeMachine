from Cappuccino import Cappuccino
from Espresso import Espresso
from Latte import Latte
from Machine import Machine


def factory(option, coffee_machine):
    if option == 1:
        return Espresso(coffee_machine.water, coffee_machine.milk,
                        coffee_machine.coffee_beans, coffee_machine.cups, coffee_machine.money)
    elif option == 2:
        return Latte(coffee_machine.water, coffee_machine.milk,
                     coffee_machine.coffee_beans, coffee_machine.cups, coffee_machine.money)
    elif option == 3:
        return Cappuccino(coffee_machine.water, coffee_machine.milk,
                          coffee_machine.coffee_beans, coffee_machine.cups, coffee_machine.money)


if __name__ == '__main__':
    isRunning = True
    machine = Machine()
    while isRunning:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            if choice != "back":
                if choice.isdigit():
                    choice_integer = int(choice)
                    if 0 < choice_integer < 4:
                        machine = factory(choice_integer, machine)
                        result = machine.make_coffee()
                        print(result)
                    else:
                        print("Choice number out of range!")
                else:
                    print("Your choice must be an integer!")
        elif action == "fill":
            water_to_add = int(input("Write how many ml of water do you want to add: "))
            milk_to_add = int(input("Write how many ml of milk do you want to add: "))
            coffee_beans_to_add = int(input("Write how many grams of coffee beans do you want to add: "))
            cups_to_add = int(input("Write how many disposable cups of coffee do you want to add: "))
            machine.add_water(water_to_add)
            machine.add_milk(milk_to_add)
            machine.add_coffee_beans(coffee_beans_to_add)
            machine.add_cups(cups_to_add)
        elif action == "take":
            machine.withdraw_money()
        elif action == "remaining":
            print(machine.get_stock())
        elif action == "exit":
            isRunning = False
        else:
            print(f"You have inputted {action}, this action is not supported!")
