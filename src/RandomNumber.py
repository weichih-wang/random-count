import random
'''
Generates a random number from 1-5 based on the probabilities below.
'''

class RandomNumber:
    """
    Class which generates number from 1-5 as stated above and stores 100
    """

    def __init__(self, store_count = 100):
        """
        store_count: keeps history of numbers up to store_count
        """
        self.store_count = store_count
        self.history = []
        self.count = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }

    def store_num(self, num):
        """
        Stores number into history.  If history is bigger than 100, remove the first element
        """
        if (not isinstance(num, int) or num < 0 or num > 5):
            raise Exception("value passed in is not an integer")
        self.history.append(num)
        self.count[num] += 1
        if (len(self.history) > self.store_count):
            rem_num = self.history.pop(0)
            self.count[rem_num] -= 1

    def get_frequency_percentage(self):
        """
        Gets the frequency percentage of each number
        """
        perc_dta = {}
        for key in self.count:
            perc = self.count[key]/len(self.history)
            perc_dta[key] = perc
        return perc_dta

    def ret_rand_num(self):
        """
        Returns a number between 1 and 5 and stores into history
        """
        rand_num = random.random()
        gen_num = self._get_num_from_percentage(rand_num)
        self.store_num(gen_num)
        return gen_num

    def _get_num_from_percentage(self, percent):
        """
        helper function to get generated number from values specified, where values are inclusive on min and exclusive on max:
        1: 0-.5
        2: .5-.75
        3 - .75-.9
        4 - .9-.95
        5 - .95-1
        """

        if  (percent >=0 and percent < .5):
            return 1
        elif (percent < .75):
            return 2
        elif (percent < .9):
            return 3
        elif (percent < .95):
            return 4
        elif (percent < 1):
            return 5
        else:
            raise Exception('not a valid number')