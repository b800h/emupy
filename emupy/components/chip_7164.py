'''
7164 Memory Chip Simulation Module

Module simulates memory chip with 8-bit data bus and 13-bit address bus. Pin-outs are as follows:


Created on 11 Aug 2014

@author: Ben Collier

'''

class chip_7164:
    
    def __init__(self, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, 
                io0, io1, io2, io3, io4, io5, io6, io7,
                not_we, not_oe, not_cs1, not_cs2):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8
        self.a9 = a9
        self.a10 = a10
        self.a11 = a11
        self.a12 = a12
        self.io0 = io0
        self.io1 = io1
        self.io2 = io2
        self.io3 = io3
        self.io4 = io4
        self.io5 = io5
        self.io6 = io6
        self.io7 = io7
        self.not_we = not_we
        self.not_oe = not_oe
        self.not_cs1 = not_cs1
        self.not_cs2 = not_cs2
        self.memory = [0] * 8192 #8192 Bytes of Memory
    
    def run_chip(self):
        
        from emupy.components.bus_unit import bus
        
        self.current_not_oe = 1
        self.current_not_we = 1
        while 1:
            if bus[self.not_oe] == 0 and self.current_not_we == 1:
                self.current_not_we = 1
                address =   bus[self.a0] + \
                            2*bus[self.a1] + \
                            4*bus[self.a2] + \
                            8*bus[self.a3] + \
                            16*bus[self.a4] + \
                            32*bus[self.a5] + \
                            64*bus[self.a6] + \
                            128*bus[self.a7] + \
                            256*bus[self.a8] + \
                            512*bus[self.a9] + \
                            1024*bus[self.a10] + \
                            2048*bus[self.a11] + \
                            4096*bus[self.a12]
                 
