class Bar():
    def __init__(self, rooms):
        self.rooms = rooms
        self.cash = 0
        self.drink_list = []
        # self.drink_list_dict = {}

    def add_money_to_till(self, amount):
        self.cash += amount

    def sell_drink(self, drink, number_sold = 1):
        self.add_money_to_till(number_sold*drink.price)
        drink.reduce_number_available(number_sold)
        # self.drink_list_dict[drink] = drink.number_available - number_sold
    
