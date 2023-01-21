# Thread Locking
# Avoiding the dreaded race conditions and deadlocks
# Race condition: same resource modified by multiple threads
# Deadlock: multiple threads waiting on the same resource


"""
Python threads can't run in parallel on mulitple CPU cores because of the global interpreter lock
"""

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0


def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting:{threadname}')

    for x in range(count):
        logging.info(f'Count: {threadname}+={count}')
        # The global interpreter lock in action
        # counter +=1
        lock = threading.Lock()
        # lock.acquire()
        # lock.acquire() deadlock
        # try:
        #     counter +=1
        # finally:
        #     lock.release()
        with lock:
            logging.info(f'Locked:{threadname}')
            counter +=1
            time.sleep(2)

    logging.info(f"Completed:{threadname}")


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')
    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers * 2):
            v = random.randrange(1, 5)
            ex.submit(test, v)
    logging.info(f"Counter:{counter}")
    logging.info("App finished")


if __name__ == "__main__":
    main()
