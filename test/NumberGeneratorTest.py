'''
Unit tests for NumberGenerator.py (problem 4)
'''
import unittest
from src.NumberGenerator import NumberGenerator
import time

class RandomNumberTest(unittest.TestCase):

    def test_thread_writer(self):
        """
        Tests if thread is writing correctly
        """
        gen = NumberGenerator(filename="testgen.log")
        gen.start_file_writer()
        num1 = gen.ret_rand_num()
        num2 = gen.ret_rand_num()
        time.sleep(2)
        with open("testgen.log", 'r') as f:
            line = f.readline()
            line2 = f.readline()
        f.close()
        print(line)
        print(line2)
        self.assertEqual(num1, int(line.split(',')[0]))
        self.assertEqual(num2, int(line2.split(',')[0]))


if __name__ == '__main__':
    unittest.main()