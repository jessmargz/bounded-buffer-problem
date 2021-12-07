# # Jessica Margala
# # CS 4310 Operating Systems
# # Project 7 - Race Conditions
# # December 6, 2021

import threading
import time
from random import seed, randint
 
# globals
n = 5
buffer = []   # large array (list) of n integers, initialzed to all zeros
for i in range(0, n):
    buffer.insert(i, 0)
next_in = 0
next_out = 0

seed(1)
 
# producer thread class
class Producer(threading.Thread):
    def run(self):

        global n, buffer, next_in, next_out
    
        while (consumer.is_alive()): 
            k1 = randint(0, 15)     # get random number k1
            print(f"Producer is now executing for a short burst of {k1} iterations.")

            for i in range(0, k1):                                                  # during each burst of length k1
                index = (next_in + 1)%n
                print(f"Producer is adding a 1 to the buffer at index {index}.")
                buffer[index] += 1                                                  # producer adds 1 to the next k1 slots of the buffer, mod n
                print(f"Current Buffer: {buffer}")
                next_in = (next_in + 1)%n
             
            t1 = randint(0,5)     # get random number t1 
            print(f"Producer is sleeping now for {t1} seconds!")
            time.sleep(t1)
             
 
# consumer thread class
class Consumer(threading.Thread):
    def run(self):
    
        global n, buffer, next_in, next_out

        while 1:
            t2 = randint(0, 5)     # get random number t1
            time.sleep(t2)    
            k2 = randint(0, 15)     # get random number k2
            print(f"Consumer is now executing for a short burst of {k2} iterations.")

            for i in range(0, k2):                       # during each burst of length k2
                index = (next_out + 1)%n
                data = buffer[index]                     # the consumer reads the next k2 slots
                buffer[index] = 0                        # and resets them to 0
                print(f"Data value is {data}.") 
                if data > 1:                             # if any slot contains a number greater than 1
                    print("Race condition found!")       # a race condition has been detected
                    exit()
                next_out = (next_out + 1)%n
                print(f"Current Buffer: {buffer}")
 
# make producer thread (process 1)
producer = Producer()
# make consumer thread (process 2)
consumer = Consumer()
 
# start the threads
consumer.start()
producer.start()
 
# wait for them to finish
producer.join()
consumer.join()
