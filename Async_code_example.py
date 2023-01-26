# Async code
# Async runs in the same thread
# Async uses Coroutines which run on the same thread
# We also introduce the async and await keywords
import random
import threading
import multiprocessing
import logging
import asyncio

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}\{threadname}:{msg}')


async def work(name):
    display(name + 'starting')
    # Without await it will jump to next line
    await asyncio.sleep(random.randint(1, 10))
    display(name + 'finished')


async def run_async(max):
    tasks = []
    for x in range(max):
        name = "Item" + str(x)
        tasks.append(asyncio.ensure_future(work(name)))

    await asyncio.gather(*tasks)

def main():
    display('Main Started')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_async(50))
    # Run forever
    # loop.run_forever()
    loop.close()
    display('Main Finished')

if __name__ == '__main__':
    main()