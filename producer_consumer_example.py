# Simple producer and consumer

# Demonstrates queue and event with locks
import random
import threading
import multiprocessing
import logging
import asyncio
import time
from threading import Thread
from queue import Queue

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}:{msg}')

#Producer
def create_work(queue,finished,max):
    finished.put(False)
    for x in range(max):
        v = random.randint(1,100)
        queue.put(v)
        display(f'Producing {x}:{v}')
    finished.put(True)
    display('finished')

# Consumer

def perform_work(work,finished):
    counter = 0
    while True:
        if not work.empty():
            v = work.get()
            display(f'Consuming {counter}: {v}')
            counter +=1
        else:
            q = finished.get()
            if q==True:
                break
            display('finished')

def main():
    max = 50
    work = Queue()
    finished = Queue()
    producer = Thread(target=create_work,args=[work,finished,max],daemon=True)
    consumer = Thread(target=perform_work,args=[work,finished],daemon=True)
    producer.start()
    consumer.start()

    producer.join()
    display("Producer has finished")
    consumer.join()
    display("Consumer has finished")
    display("Main Thread done")


if __name__=="__main__":
    main()