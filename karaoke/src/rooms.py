import random

class Rooms():
    def __init__(self, entry_fee):
        self.entry_fee = entry_fee
        self.songs = []
        self.guests = []
        self.room_size = 2

    def check_if_space_for_new_guests(self, new_guest_number = 1):
        return self.room_size > new_guest_number + len(self.guests)

    def check_in_guest(self, guest, bar, guest_number = 1): 
        for room in bar.rooms:
            if self.check_if_space_for_new_guests(guest_number):
                self.guests.append(guest)
                guest.spend_cash(self.entry_fee)
                bar.add_money_to_till(self.entry_fee)
                return
        return "All the rooms are full"
    

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song.name)

    def play_random_song(self):
        return self.songs[random.randrange(0, len(self.songs))]
        