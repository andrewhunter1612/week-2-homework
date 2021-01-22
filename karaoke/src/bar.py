class Bar:
    def __init__(self, rooms):
        self.rooms = rooms
        self.cash = 0

    def add_money_to_till(self, amount):
        self.cash += amount