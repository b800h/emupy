'''
Created on 17 Aug 2014

@author: BCollier
'''

from emupy.components import chip_7164

bus = {
       'A0': 0, 'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0,
       'A8': 0, 'A9': 0, 'A10': 0, 'A11': 0, 'A12': 0, 'A13': 0, 'A14': 0, 'A15': 0,
       'D0': 0, 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0,
       'CLK': 0, 'NOT_WE': 0, 'NOT_OE': 0, 'NC': 0 
};

memchip = chip_7164.chip_7164('A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'IO0', 'IO1', 'IO2', 'IO3', 'IO4', 'IO5', 'IO6', 'IO7', 'NOT_WE', 'NOT_OE', 'NC', 'NC')

