from Machine import Machine


class Latte(Machine):

    def __init__(self, water, milk, beans, cups, money):
        super().__init__(water, milk, beans, cups, money)
        self.required_water = 350
        self.required_milk = 75
        self.required_coffee_beans = 20
        self.cost = 7
