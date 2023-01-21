# Logging basics

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging


# from logging import root

def test():
    print('-' * 20)
    print(logging.getLevelName(logging.getLogger().getEffectiveLevel()))
    logging.debug('debug message here')
    logging.info('info message here')
    logging.warning("Warning message here")
    logging.error("Error message here")
    logging.critical("Critical message here")
    print('' * 20)


test()

# Logging levels
# Getting and setting the logging levels
# Allows for filtering

# Get the root logger
rootlog = logging.getLogger()
print('Level:' + logging.getLevelName(rootlog.getEffectiveLevel()))

# Set it to debug
rootlog.setLevel(logging.DEBUG)
test()

# Set it to Critical
rootlog.setLevel(logging.CRITICAL)
test()

# Log to file
# basicConfig only works if the logger has not been configured before
# logging.basicConfig(filename="app.txt",filemode='w',format='%(levelname)s:%(message)s',level=logging.DEBUG)
# logging.debug("Hello")

handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug("helo")
test()
