'''
Created on 17 Aug 2014

@author: BCollier
'''

from emupy.components import chip_7164
from emupy.components.bus_unit import bus 
import thread # replace with threading module

memchip = chip_7164.chip_7164('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'IO0', 'IO1', 'IO2', 'IO3', 'IO4', 'IO5', 'IO6', 'IO7', 'NOT_WE', 'NOT_OE', 'NC', 'NC')
thread.start_new_thread(memchip.run_chip(), ("Memory Chip", 2, ) )
