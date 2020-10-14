from  fish import Fish,White_Shark,Blue_Whale
from unittest import TestCase
class TestFish(TestCase):
    def test_size(self):
        new_shark = White_Shark('кожа','плавники','жабры','острые зубы')
        self.assertEqual(new_shark.size,6)
