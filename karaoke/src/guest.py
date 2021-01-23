class Guest:
    def __init__(self, name, cash, favourite_song):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song
    
    def spend_cash(self, bar):
        self.cash -= bar

    def get_total_cash(self):
        return self.cash

    def check_favourite_song(self, room):
        if self.favourite_song == room.play_random_song():
            return "yay, my favourite song"
            