import unittest

from src.guest import *
from src.songs import *
from src.rooms import *

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Andrew", 10, "song_name")
        self.song_name = Songs("song_name")
        self.room = Rooms(3, 4)
    
    def check_room_details(self):
        self.assertEqual(3, self.room.number_of_rooms)
        self.assertNotEqual(4, self.room.number_of_rooms)
        self.assertEqual(4, self.room.entry_fee)
        self.assertNotEqual(23, self.room.entry_fee)

        room.check_in_guest(self.guest)
        self.assertEqual(7, self.guest.cash)


