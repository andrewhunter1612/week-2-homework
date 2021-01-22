import unittest

from src.guest import *
from src.songs import *
from src.rooms import *
from src.bar import *

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Andrew", 10, "song_name")
        self.song_name = Songs("song_name")
        self.room = Rooms(3)
        self.bar = Bar([self.room, self.room])


    def test_guest_details(self):
        #init test
        self.assertEqual("Andrew", self.guest.name)
        self.assertNotEqual("James", self.guest.name)
        self.assertEqual(10, self.guest.cash)
        self.assertNotEqual(5, self.guest.cash)
        self.assertEqual("song_name", self.guest.favourite_song)
        self.assertNotEqual("not a song", self.guest.favourite_song)

        #check favourite song
        self.room.add_song_to_room(self.song_name)
        self.assertEqual("yay, my favourite song", self.guest.          check_favourite_song(self.room))

