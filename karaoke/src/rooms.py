import random
from src.bar import Bar

class Rooms(Bar):
    def __init__(self, entry_fee):
        self.entry_fee = entry_fee
        self.songs = []
        self.guests = []
        self.room_size = 10

    def check_if_space_for_new_guests(self, new_guest_number = 1):
        return self.room_size > new_guest_number + len(self.guests)

    def check_in_guest(self, guest, guest_number = 1): 
        if self.check_if_space_for_new_guests(guest_number):
            self.guests.append(guest)
            guest.spend_cash(self.entry_fee)
            
        else:
            return "No room in the inn"
            #need to put them in a new room
        

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def choose_random_song(self, song):
        return self.songs[random.randrange(0, len(self.songs))]
        