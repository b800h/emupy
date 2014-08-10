'''
Created on 10 Aug 2014

@author: BCollier
'''

VERSION = 0.1

class clock:
    def __init__ (self):
        self.cycle = 0
    def tick (self):
        self.cycle = self.cycle + 1

if __name__ == '__main__':
    pass

print "EmuPy v" + str(VERSION) + " initialising..."

clock1 = clock()

print "EmuPy running. Press CTRL-C to end emulation."

while 1:
    clock1.tick


