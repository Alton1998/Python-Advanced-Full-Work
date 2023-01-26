# Intro to multiprocessing
# multiple processe running the same script
# this is very different from threading
# Each process has its own memory space, and its own threads

import logging
import multiprocessing
from multiprocessing import process
import time


# Process starting function
def run(num):
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    time.sleep(num * 2)
    logging.info(f'Finished {name}')


# Basic process usage

def main():
    logging.info('Starting')
    name = process.current_process().name
    logging.info(f' Running {name} as {__name__}')
    processes = []

    for x in range(5):
        p = multiprocessing.Process(target=run,args=[x],daemon=True)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


    logging.info(f'Finished {name}')


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == "__main__":
    main()
