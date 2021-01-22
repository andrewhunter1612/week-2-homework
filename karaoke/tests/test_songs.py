import unittest

from src.guest import *
from src.songs import *
from src.rooms import *

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song_name = Songs("song_name")

    def test_song_details(self):
        self.assertEqual("song_name", self.song_name.name)




