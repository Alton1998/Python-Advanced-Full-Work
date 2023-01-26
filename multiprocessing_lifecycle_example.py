# Multiprocess starting and stopping
# The full life cycle

import logging
import multiprocessing
from multiprocessing.context import Process
import time


def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f'{name} started')
    for x in range(max):
        logging.info(f'{name} {msg}')
        time.sleep(1)


def main():
    logging.info('Started')
    max = 15
    worker = Process(target=work, args=['Worker', max], daemon=True, name='Worker')
    worker.start()
    time.sleep(5)

    if worker.is_alive:
        worker.terminate()
    worker.join()
    logging.info(f'Finished:{worker.exitcode}')


logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == "__main__":
    main()
