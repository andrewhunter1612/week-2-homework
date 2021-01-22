import unittest

from src.guest import *
from src.songs import *
from src.rooms import *

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Andrew", 10, "song_name")
        self.song_name = Songs("song_name")
        self.room = Rooms(3, 3)

    def test_song_details(self):
        self.assertEqual("song_name", self.song_name.name)




