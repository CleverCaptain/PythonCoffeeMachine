from Machine import Machine


class Espresso(Machine):

    def __init__(self, water, milk, beans, cups, money):
        super().__init__(water, milk, beans, cups, money)
        self.required_water = 250
        self.required_milk = 0
        self.required_coffee_beans = 16
        self.cost = 4
