'''
Created on 17 Aug 2014

@author: BCollier
'''

from emupy.components import chip_7164
from emupy.components.bus_unit import bus
import time
from emupy.emu import setaddressbus, setdatabus, getaddressbus, getdatabus


memchip1 = chip_7164.chip_7164(1, "Memory Chip 1", 2, 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'IO0', 'IO1', 'IO2', 'IO3', 'IO4', 'IO5', 'IO6', 'IO7', 'NOT_WE', 'NOT_OE', 'NC', 'NC')
#memchip2 = chip_7164.chip_7164(2, "Memory Chip 2", 2, 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'IO0', 'IO1', 'IO2', 'IO3', 'IO4', 'IO5', 'IO6', 'IO7', 'NOT_WE', 'NOT_OE', 'NC', 'NC')

memchip1.start()
#memchip2.start()

bus["NOT_OE"] = 1
time.sleep(4)

setdatabus(0xaa)

bus["A6"] = 1
time.sleep(4)
bus["NOT_WE"] = 1
bus["NOT_OE"] = 1
time.sleep(4)
bus["NOT_WE"] = 0
time.sleep(4)

setdatabus(0x00)
print "Current data bus:" + str(getdatabus())

bus["A6"] = 1
time.sleep(4)
bus["NOT_WE"] = 1
bus["NOT_OE"] = 1
time.sleep(4)
bus["NOT_OE"] = 0

print "Data bus output: " + hex(getdatabus())

# create function to set address or data bus using a single hex value