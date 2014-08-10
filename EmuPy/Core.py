'''
Created on 10 Aug 2014

@author: BCollier
'''

import time

VERSION = 0.1

class clock:
    def __init__ (self, speed):
        self.lasttime = time()
        self.cycle = 0
        self.normalinterval = 1 / (speed * 1000000)
    def tick (self):
        self.cycle = self.cycle + 1
    def run(self):
        self.thistime = time()
        self.interval = self.thistime - self.lasttime
        if self.interval > self.normalinterval:
            self.tick     

if __name__ == '__main__':
    pass

print "EmuPy v" + str(VERSION) + " initialising..."

clock1 = clock(4.77) # Instantiate clock running at 4.77 MHz

print "EmuPy running. Press CTRL-C to end emulation."

while 1:
    clock1.run