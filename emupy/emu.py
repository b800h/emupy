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