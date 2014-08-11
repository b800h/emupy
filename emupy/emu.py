'''
Created on 10 Aug 2014

@author: BCollier
'''

import time
import components.chip_4164

# Config Items

VERSION = 0.1

# Global System Considerations - Farm this out to System Config Python File

bus = {
       'A0': 0, 'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0,
       'A8': 0, 'A9': 0, 'A10': 0, 'A11': 0, 'A12': 0, 'A13': 0, 'A14': 0, 'A15': 0,
       'D0': 0, 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0,
       'CLK': 0
};

# Clock object - Add this to clock.py

class clock:
    def __init__ (self, speed):
        self.lasttime = time.clock() #Use time.time() on Linux
        self.cycle = 0
        self.speed = speed
        self.normalinterval = 1 / (speed * 100000)
        print "Clock running at " + str(self.speed) + "MHz"
        print "Internal clock interval: " + str(self.normalinterval) + " seconds."
        self.clockwave = True
    def tick (self):
        self.cycle = self.cycle + 1
        self.clockwave = not self.clockwave
            
    def run(self):
        self.thistime = time.clock() #Use time.time() on linux
        self.interval = self.thistime - self.lasttime
        if self.interval > self.normalinterval:
            self.lasttime = self.thistime
            self.tick()

if __name__ == '__main__':
    pass

print "EmuPy v" + str(VERSION) + " initialising..."

clock1 = clock(4.77) # Instantiate clock running at 4.77 MHz

print "EmuPy running. Press CTRL-C to end emulation."
breakflag = 0

while breakflag == 0:
    currentwave = clock1.clockwave
    clock1.run()
    if currentwave <> clock1.clockwave:
        print "Up"