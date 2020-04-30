import datetime
import random
from src.task2 import task2
import unittest
import pandas as pd


class Test(unittest.TestCase):
    def generate_time_series(self, N):
        '''
        Creates two lists representing time-series data on second basis with random variable
        :param N: size of dataset to generate
        :return: time_series unary data
        '''
        t0 = datetime.datetime.now()
        result = []
        delta = datetime.timedelta(seconds=1)
        for _ in range(N):
            result.append((t0, random.randint(0, 100)))
            t0 = t0 + delta
        return list(zip(*result))

    def test_statistics(self, window_size):
        '''
        General sanity check function for calculated statistics
        :param window_size: size upon which statistics is calculated
        '''
        for n in range(window_size * 2, window_size * 4, window_size):
            ds = self.generate_time_series(n)
            result = task2(ds, w_size=window_size)
            s = pd.Series(ds[1])
            m = list(s.rolling(window_size).mean().dropna()[:-1])
            med = list(s.rolling(window_size).median().dropna()[:-1])
            max = list(s.rolling(window_size).max().dropna()[:-1])
            min = list(s.rolling(window_size).min().dropna()[:-1])
            self.assertListEqual(list(result[0]), m)
            self.assertListEqual(list(result[1]), med)
            self.assertListEqual(list(result[2]), max)
            self.assertListEqual(list(result[3]), min)

    def test1(self):
        '''
 Testing values on 100 sec samples
        '''
        window_size = 100
        self.test_statistics(window_size)

    def test2(self):
        '''
        Testing stats on daily basis
        '''
        window_size = 60*60
        self.test_statistics(window_size)



