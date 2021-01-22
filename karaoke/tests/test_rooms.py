import unittest

from src.guest import *
from src.songs import *
from src.rooms import *
from src.bar import *

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Andrew", 10, "song_name")
        self.song_name = Songs("song_name")
        self.room = Rooms(3)
        self.bar = Bar(self.room)

    
    def test_check_room_details(self):
        #check init is working
        self.assertEqual(3, self.room.entry_fee)
        self.assertNotEqual(23, self.room.entry_fee)

        #check guest cash removed is equal to the entry fee 
        self.room.check_in_guest(self.guest, 1)
        self.assertEqual(7, self.guest.cash)
        self.assertEqual("No room in the inn", self.room.check_in_guest(self.guest, 100))

        self.assertEqual(1, len(self.room.guests))
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))


