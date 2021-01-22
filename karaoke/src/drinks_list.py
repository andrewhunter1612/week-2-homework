class DrinksList():
    def __init__(self, name, price, number_available):
        self.name = name
        self.price = price
        self.number_available = number_available

    def reduce_number_available(self, number_sold):
        self.number_available -= number_sold

    def purchased_new_stock(self, number_purchased):
        self.number_available += number_purchased

    def change_price(self, new_price):
        self.price = new_price