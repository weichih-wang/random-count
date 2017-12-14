'''
Unit tests for RandomNumber.py (problem 2)
'''
import unittest
from src.RandomNumber import RandomNumber

class RandomNumberTest(unittest.TestCase):

    def test_frequency_percentage(self):
        """
        Checks if frequency calculation is correct
        """
        ran_num = RandomNumber()
        for x in range(10):
            ran_num.ret_rand_num()
        result = ran_num.get_frequency_percentage()
        calc_result = {1:0,2:0,3:0,4:0,5:0}
        for x in range(len(ran_num.history)):
            calc_result[ran_num.history[x]]+=1
        self.assertEqual(result[1], calc_result[1]/len(ran_num.history))
        self.assertEqual(result[2], calc_result[2]/len(ran_num.history))
        self.assertEqual(result[3], calc_result[3]/len(ran_num.history))
        self.assertEqual(result[4], calc_result[4]/len(ran_num.history))
        self.assertEqual(result[5], calc_result[5]/len(ran_num.history))
        
    def test_wrap(self):
        """
        Checks to see if most recent numbers are stored
        """
        ran_num = RandomNumber()
        for x in range(100):
            ran_num.ret_rand_num()
        new_num = ran_num.ret_rand_num()
        self.assertEqual(new_num, ran_num.history[-1])



if __name__ == '__main__':
    unittest.main()