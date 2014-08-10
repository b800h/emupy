'''
Created on 10 Aug 2014

@author: BCollier
'''

import time

VERSION = 0.1

class clock:
    def __init__ (self, speed):
        self.lasttime = time.clock() #Use time.time() on Linux
        self.cycle = 0
        self.speed = speed
        self.normalinterval = 1 / (speed * 1000000)
        print "Clock running at " + str(self.speed) + "MHz"
        print "Internal clock interval: " + str(self.normalinterval) + " seconds."
    def tick (self):
        self.cycle = self.cycle + 1
        if self.cycle == 4770000:
            self.cycle = 0
            # print "Second"
            
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
    clock1.run()