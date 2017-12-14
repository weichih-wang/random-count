'''
Unit tests for RandomNumberFunction.py (problem 1)
'''
import unittest
from src import RandomNumberFunction

class RandomNumberFunctionTest(unittest.TestCase):

    def test_get_num_from_percentage(self):
        self.assertEqual(1, RandomNumberFunction.get_num_from_percentage(0.01))
        self.assertEqual(2, RandomNumberFunction.get_num_from_percentage(0.51))
        self.assertEqual(3, RandomNumberFunction.get_num_from_percentage(0.76))
        self.assertEqual(4, RandomNumberFunction.get_num_from_percentage(0.901))
        self.assertEqual(5, RandomNumberFunction.get_num_from_percentage(0.951))
        with self.assertRaises(Exception):
            RandomNumberFunction.test_get_num_from_percentage(0);

if __name__ == '__main__':
    unittest.main()