# Daemon threads
# Quitting when we quit the app

import logging
import threading
from threading import Thread, Timer
import time


def test():
    threadname = threading.current_thread().name
    logging.info(f'Starting :{threadname}')
    for x in range(60):
        logging.info(f'Working:{threadname}')
        time.sleep(1)
    logging.info(f'Finished:{threadname}')

def stop():
    logging.info('Exiting the application')
    exit(0)

# Main Function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main thread Starting')

    timer = Timer(3,stop)
    timer.start()

    # t = Thread(target=test,daemon=False)
    t = Thread(target=test, daemon=True)
    t.start()

    logging.info("Main thread Finished")

if __name__ == '__main__':
    main()