# Queues and Future

# Getting values from a thread
# This is a problem for future

"""
Queues is like leaving a message
A Future is used for synchronizing program execution
in some concurrent programming languages. They describe an
objaect that acts a proxy for a result that is initially unknown.
usually because the computation of its value is not yet complete
"""

import logging
import threading
from threading import Thread
import time
import random
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

#Queues
# Use queue to pass messages back and forths

def test_que(name, que):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finsished:{threadname}')
    ret = "Hello" + name +" your random number is:" + str(random.randrange(1,10))
    que.put(ret)

def queued():
    que = Queue()
    t = Thread(target=test_que,args=['Alton',que])
    t.start()
    logging.info("Do something on the main thread")
    t.join()
    ret = que.get()
    logging.info(f'Returned:{ret}')

#Futures
#Use futures, easier and cleaner
def test_future(name):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finsished:{threadname}')
    ret = "Hello" + name +" your random number is:" + str(random.randrange(1,10))
    return ret

def pooled():
    workers = 20
    ret =[]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(test_future,"Alton" + str(x))
            ret.append(future)
    logging.info('Do something on the main thread')
    for r in ret:
        logging.info(f"Returned:{r.result()}")

#Main Function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting app')
    # queued()
    pooled()
if __name__ == "__main__":
    main()