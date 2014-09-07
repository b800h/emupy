'''

--------------=====Resource Library=====-----------------

Created on 10 Aug 2014

@author: BCollier

This module contains shared library function

Initial list follows

decodebus()
rotate_right_8()    rotate an eight-bit number right
rotate_left_8()     rotate an eight-bit number left
not_8()             logical not on an 8-bit number
and_8()             logical and on an 8-bit number
or_8()              logical or on an 8-bit number
xor_8()             logical xor on an 8-bit number
nand_8()            logical nand on an 8-bit number

---------------------------------------------------------

'''

from emupy.components import bus_unit

def setaddressbus(value):
    m=0
    #print str(bin(value))
    for n in reversed(bin(value)[2:]):
        bus_unit.bus['A' + str(m)] = n
        print "Address bus pin " + str(m) + " set to " + str(n)
        m = m + 1
    #Then fill remains with blanks
        
def getaddressbus():
    m = 1
    total = 0
    for n in range(0,12):
        total = total + int(int(bus_unit.bus['A' + str(n)]) * m)
        m = m * 2
    return total

def getdatabus():
    m = 1
    total = 0
    for n in range(0,8):
        total = total + int(int(bus_unit.bus['D' + str(n)]) * m)
        m = m * 2
    return total
         
def setdatabus(value):
    m=0
    for n in reversed(bin(value)[2:]):
        bus_unit.bus['D' + str(m)] = n
        print "Data bus pin " + str(m) + " set to " + str(n)
        m = m + 1
    #Then fill remains with blanks
    print bin(value)[2:]
    while m < 8:
        bus_unit.bus['D' + str(m)] = 0
        m = m + 1

def decodebus(o1,o2,o3,o4,o5,o6,o7,o8):
    return   int(o1) + \
            int(2*o2) + \
            int(4*o3) + \
            int(8*o4) + \
            int(16*o5) + \
            int(32*o6) + \
            int(64*o7) + \
            int(128*o8) #+ \
            #int(256*bus[self.a8]) + \
            #int(512*bus[self.a9]) + \
            #int(1024*bus[self.a10]) + \
            #int(2048*bus[self.a11]) + \
            #int(4096*bus[self.a12])
            
def clockdown():
    bus_unit.bus['CLK'] = 0
    #print "Clock down. Clock is now " + str(bus_unit.bus['CLK'])

def clockup():
    bus_unit.bus['CLK'] = 1
    #print "Clock up. Clock is now " + str(bus_unit.bus['CLK'])
    
def clocktoggle():
    bus_unit.bus['CLK'] = not(bus_unit.bus['CLK'])
    #print "Clock toggled. Clock is now " + str(bus_unit.bus['CLK'])