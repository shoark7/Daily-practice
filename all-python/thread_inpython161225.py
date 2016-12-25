"""
Now it's time for me to start thread in Python.
I have to start from scratch so let's start step by step.

Start date = 2016/12/25
End date = 201?/??/??
"""

import time
import threading
import datetime

# In python, threading module is almost what we're looking for.
# It means there are also other options but not recommended.


##################### Step 1. ###################
################## very basic ###################
#################################################

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            time.sleep(0.1)


send = Messenger(name='Sending out messages')
receive = Messenger(name='Receiving out messages')

send.start()
receive.start()

"""
In Pyhton, you have to override run method to get your thread started.
start method executes run method.
"""


##################### Step 2. ###################
################## Another example ##############
#################################################

class TimeThread(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print('Hello world! Its {} and {} now!'.format(self.getName(), now))


for _ in range(3):
    t = TimeThread()
    t.start()
