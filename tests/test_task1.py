import random
import unittest
from src.task1 import task1


class Test(unittest.TestCase):
    def generate_random_list(self, n):
        randomList = []
        # Set a length of the list to 10
        for i in range(0, n):
            # any random numbers from 0 to 1000
            randomList.append(random.randint(0, 30))
        return randomList

    def test1(self):
        for i in range(10, 200, 10):
            result_len = i/10
            rand_list = self.generate_random_list(i)
            result = task1(rand_list, result_len)
            self.assertEqual(len(result), result_len)




