'''
Created on 7 Sep 2014

@author: BCollier

Basic code test to run a simple native function. Assembly to run a loop is as follows:

Count to ten. Equiv in x86 asm:

start:
mov ax, 10
dec ax
cmp ax,0
jne start

lde 10
cae 1
jnz 0x00

So: we need instructions lde, cae, jnz



'''

import emupy.emu
from emupy.components import chip_8060, chip_7164
from emupy.components.bus_unit import bus
import time

cpu = chip_8060.chip_8060(1, "CPU", 
                          "", "", "", "", "", "", "", "",
                          "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0",
                          "", "", "", "", "", "", "", "CLK",
                          "A11", "A10", "A9", "A8", "A7", "A6", "A5", "A4", "A3", "A2", "A1", "A0",
                          "", "", "", "")

memchip1 = chip_7164.chip_7164(1, "64Kb RAM", 2, 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'IO0', 'IO1', 'IO2', 'IO3', 'IO4', 'IO5', 'IO6', 'IO7', 'NOT_WE', 'NOT_OE', 'NC', 'NC')

cpu.start()
emupy.emu.setdatabus(0x08)
while 1:
    time.sleep(0.01)
    emupy.emu.clockup()
    time.sleep(0.01)
    emupy.emu.clockdown()
    print emupy.emu.getaddressbus()
