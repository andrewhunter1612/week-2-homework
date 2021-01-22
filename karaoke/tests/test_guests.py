import unittest

from src.guest import *
from src.songs import *
from src.rooms import *

class TestGuests(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Andrew", 10, "song_name")
        self.song_name = Songs("song_name")

    def test_guest_details(self):
        self.assertEqual("Andrew", self.guest.name)
        self.assertNotEqual("James", self.guest.name)
        self.assertEqual(10, self.guest.cash)
        self.assertNotEqual(5, self.guest.cash)
        self.assertEqual("song_name", self.guest.favourite_song)
        self.assertNotEqual("not a song", self.guest.favourite_song)

        # self.song_name
        # self.assertEqual("yay, my favourite song", self.guest.          check_favourite_song(self.song_name))

