'''
from datetime import datetime
from time import sleep
from random import randint

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

for i in range(5):
    if right_this_minute in odds:
        print("this minute seems a little odd")
    else:
        print("not an odd minute")
    wait_time = randint(1,60)
    sleep(wait_time)
'''
# the code below does exactly the same as the one above, i just tweaked it to be like the example in the book

from datetime import datetime
import time
import random

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute = datetime.today().minute

for i in range(5):
    if right_this_minute in odds:
        print("this minute seems a little odd")
    else:
        print("not an odd minute")
    wait_time = random.randint(1,60)
    time.sleep(wait_time)

