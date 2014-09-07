'''
Created on 7 Sept 2014

@author: BCollier
'''

''''
This test executes a "free run", on the chip, by placing the code for
a "nop" on the data bus and letting the machine cycle through the available
address range.
'''

import emupy.emu
from emupy.components import chip_8060
from emupy.components.bus_unit import bus
import time

cpu = chip_8060.chip_8060(1, "CPU", 
                          "", "", "", "", "", "", "", "",
                          "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0",
                          "", "", "", "", "", "", "", "CLK",
                          "A11", "A10", "A9", "A8", "A7", "A6", "A5", "A4", "A3", "A2", "A1", "A0",
                          "", "", "", "")


cpu.start()
emupy.emu.setdatabus(0x08)
time.sleep(2)
emupy.emu.clockup()
time.sleep(2)
emupy.emu.clockdown()
time.sleep(2)
emupy.emu.clockup()
time.sleep(2)
emupy.emu.clockdown()