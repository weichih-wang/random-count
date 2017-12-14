import random

'''
Prints a number between 1 and 5 where the probabilities of each number are:
1 - 50%
2 - 25%
3 - 15%
4 - 5%
5 - 5%
'''
def print_rand_num():
    rand_num = random.random()
    print (get_num_from_percentage(rand_num))

'''
helper function to get generated number from values specified, where values are inclusive on min and exclusive on max:
1: 0-.5
2: .5-.75
3 - .75-.9
4 - .9-.95
5 - .95-1
'''
def get_num_from_percentage(percent):
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