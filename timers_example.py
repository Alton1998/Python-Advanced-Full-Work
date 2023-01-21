# Timers
# Execute code at timed intervals
# This is the first step in learning threadign

# imports and display

import time
from threading import Timer


def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))


def run_once():
    display('Run once:')
    t = Timer(5,display,['Timeout:'])
    t.start() # run is called

run_once()
# Notice this runs immediately
# But it also runs once
print('waiting')

# Interval timer
# Wrap it into a class
# Make it run untill we stop it
# Notice we can have multiple timers at once

class RepeatTimer(Timer):
    def run(self) -> None:
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)
        print('Done')

timer = RepeatTimer(1 ,display,['Repeating'])
timer.start() # going to call run
print('Threading started')
time.sleep(10)
print('threading finished')
timer.cancel()