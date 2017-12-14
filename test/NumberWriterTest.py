'''
Unit tests for NumberWriter.py (problem 5)
'''
import unittest
from src.NumberWriter import NumberWriter
import time

class RandomNumberTest(unittest.TestCase):

    def test_thread_writer(self):
        """
        Tests if thread is writing correctly
        """
        gen = NumberWriter(filename="testfive.log")
        linecount = sum(1 for line in open('testfive.log'))
        self.assertEqual(25, linecount)


if __name__ == '__main__':
    unittest.main()