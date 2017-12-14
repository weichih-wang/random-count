import random
import datetime
import time
from queue import Queue
import threading

'''
Modified class of RandomNumber for Problem 4 down.  I'm unsure if this is what the prompt is asking me to do.  Please let me knkow
if my assumption is wrong and I am suppose to modify the other class.
'''

class NumberGenerator:
    """
    Class which generates number from 1-5 as stated above and stores 100
    """

    def __init__(self, filename="numbers.log"):
        """
        store_count: keeps history of numbers up to store_count
        """
        self.filename = filename
        self.queue = Queue()

    def ret_rand_num(self):
        """
        Returns a number between 1 and 5 and stores into history
        """
        rand_num = random.random()
        gen_num = self._get_num_from_percentage(rand_num)
        self.queue.put((gen_num,datetime.datetime.now()))
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

    def start_file_writer(self):
        """
        Thread which writes queue values into file
        """
        t = threading.Thread(target=self.write_to_file_worker)
        t.daemon = True
        t.start()

    def write_to_file_worker(self):
        """
        Writes number and time to file
        """
        count = 0
        while True:
            item = self.queue.get()
            #stop running file worker thread if no numbers have come in for more than 5 sec
            if (count == 5):
                break
            if item is None:
                time.sleep(1)
                count += 1
            else:
                count = 0
                with open(self.filename, 'a') as f:
                    f.write('{},{}\n'.format(item[0],item[1]))
                f.close()

    def generateNum(self):
        """
        generates a number every 2 seconds
        """
        while True:
            self.ret_rand_num()
            time.sleep(2)