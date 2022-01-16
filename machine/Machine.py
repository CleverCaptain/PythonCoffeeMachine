class Machine:
    required_water = 0
    required_milk = 0
    required_coffee_beans = 0
    cost = 0

    def __init__(self, water = 400, milk = 540, beans = 120, cups = 9, money = 550):
        self.water = water
        self.milk = milk
        self.coffee_beans = beans
        self.cups = cups
        self.money = money

    def add_water(self, water_to_add):
        self.water += water_to_add

    def add_milk(self, milk_to_add):
        self.milk += milk_to_add

    def add_coffee_beans(self, coffee_beans_to_add):
        self.coffee_beans += coffee_beans_to_add

    def add_cups(self, cups_to_add):
        self.cups += cups_to_add

    def withdraw_money(self):
        print("I gave you $", self.money)

    def make_coffee(self):
        result = self.has_enough_resources()
        if result == "I have enough resources, making you a coffee!":
            self.use_water()
            self.use_milk()
            self.use_coffee_beans()
            self.use_cups()
            self.receive_money()
            return result
        else:
            return result

    def use_water(self):
        self.water -= self.required_water

    def use_milk(self):
        self.milk -= self.required_milk

    def use_coffee_beans(self):
        self.coffee_beans -= self.required_coffee_beans

    def use_cups(self):
        self.cups -= 1

    def has_enough_resources(self):
        if self.water < self.required_water:
            return "Sorry, not enough water!"
        elif self.milk < self.required_milk:
            return "Sorry, not enough milk!"
        elif self.coffee_beans < self.required_coffee_beans:
            return "Sorry, not enough CoffeeBeans!"
        elif self.cups < 1:
            return "Sorry, not enough cups!"
        else:
            return "I have enough resources, making you a coffee!"

    def receive_money(self):
        self.money += self.cost

    def get_stock(self):
        return f"The coffee machine has:\n" \
               f"{self.water} of water\n" \
               f"{self.milk} of milk\n" \
               f"{self.coffee_beans} of coffee beans\n" \
               f"{self.cups} of cups\n" \
               f"{self.money} of money"
