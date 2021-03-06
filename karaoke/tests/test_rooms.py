import unittest

from src.guest import *
from src.songs import *
from src.rooms import *
from src.bar import *
from src.drinks_list import *

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Andrew", 10, "song_name")
        self.song_name = Songs("song_name")
        self.room = Rooms(3, 4)
        self.bar = Bar([self.room, self.room])
        self.drinks = DrinksList("beer", 2, 20)

    
    def test_check_room_details(self):
        #check init is working
        self.assertEqual(3, self.room.entry_fee)
        self.assertNotEqual(23, self.room.entry_fee)

        #check in guest function
        self.room.check_in_guest(self.guest, self.bar)
        self.assertEqual(7, self.guest.cash)
        self.assertEqual("All the rooms are full", self.room.check_in_guest(self.guest, self.bar, 100))
        self.assertEqual(None, self.room.check_in_guest(self.guest, self.bar))
        self.assertEqual(2, len(self.room.guests))
        self.assertEqual(6, self.bar.cash)

        #check out guest function
        self.room.check_out_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

        #add song to room
        self.room.add_song_to_room(self.song_name)
        self.assertEqual("song_name", self.room.songs[0])



