import random
import datetime
import time
from queue import Queue
import threading

'''
Modified class of RandomNumber for Problem 5 down.  I'm unsure if this is what the prompt is asking me to do.  Please let me knkow
if my assumption is wrong and I am suppose to modify the other class.
'''

class NumberGenerator:
    """
    Class which generates number from 1-5 as stated above and stores 100
    """
    def ret_rand_num(self):
        """
        Returns a number between 1 and 5 and stores into history
        """
        rand_num = random.random()
        gen_num = self._get_num_from_percentage(rand_num)
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

    def generate_numbers(self, send_num_function, runtime=5):
        """
        generates a number every 1 second and passes generated number and timestamp (format: time, number) to send_num_function.
        Stops at 5 by default (denoted by runtime)
        """
        count = 0
        while True and count < runtime:
            send_num_function((time.time(), self.ret_rand_num()))
            time.sleep(1)
            count += 1