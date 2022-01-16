from Machine import Machine


class Cappuccino(Machine):

    def __init__(self, water, milk, beans, cups, money):
        super().__init__(water, milk, beans, cups, money)
        self.required_water = 200
        self.required_milk = 100
        self.required_coffee_beans = 12
        self.cost = 6
