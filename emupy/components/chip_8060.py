'''
----------------------------------------

Created on 19 Aug 2014

@author: BCollier

INS8060 Chip Implementation (SC/MP)

---------===Instruction Set===----------

m is the mode bit. If 1 the instruction is auto-indexed, if 0 it is indexed. pp refers to a pointer register, P0..P3

If mpp is 100 (you can't auto index on the program counter), this is immediate mode. The data is in the next byte ( ). There is, of course, no store immediate.

****Double Byte Instructions****

LD/LDI         11000mpp dddddddd     18/10     AC := (EA)
ST             11001mpp dddddddd     18/10     (EA) := ACOR
AND/ANI        11010mpp dddddddd     18/10     AC := AC & (EA)
OR/ORI         11011mpp dddddddd     18/10     AC := AC | (EA)
XOR/XRI        11100mpp dddddddd     18/10     AC := AC ^ (EA)
DAD/DAI (1)    11101mpp dddddddd     23/15     AC,CYL := AC+(EA)+CY/L, base 10
ADD/ADI        11110mpp dddddddd     19/11     AC,CYL := AC+(EA)+CY/L
CAD/CAI (2)    11111mpp dddddddd     20/12     AC,CYL := AC+~(EA)+CY/L
ILD            101010pp dddddddd     22        AC,(EA) := (EA)+1
DLD            101110pp dddddddd     22        AC,(EA) := (EA)-1
JMP            100100pp dddddddd     9         PC := EA
JP             100101pp dddddddd     9/11      if AC > 0 PC := EA
JZ             100110pp dddddddd     9/11      if AC = 0 PC := EA
JNZ            100111pp dddddddd     9/11      if AC <> 0 PC := EA
DLY            10001111 dddddddd     (3)       Delay

(1) DAD and DAI are decimal add instructions. These do not affect the overflow

(2) CAD and CAI are complement and add instructions, these are used to subtract.

(3) Delays for 13 + 2 * AC + 2 * dddddddd + 2^9 * dddddddd cycles. (13-131,593), AC is set to -1 afterwards.

****Single Byte Instructions****

lde     01000000     6     AC := E
xae     00000001     7     AC <-> E
ane     01010000     6     AC := AC & E
ore     01011000     6     AC := AC | E
xre     01100000     6     AC := AC ^ E
dae     01101000     11     AC := AC + E + CY/L base 10 
ade     01101000     7     AC := AC + E + CY/L
cae     01111000     8     AC := AC + ~E + CY/L
xpal     001100pp     8     AC <-> P.Low
xpah     001101pp     8     AC <-> P.High
xppc     011111pp     7     P <-> P0
sio     00011001     5     Sout := E0,E := E >> 1, E7 := Sin
sr     00011100     5     AC := AC >> 1
srl     00011101     5     AC := AC >> 1,AC7 := CY/L
rr     00011110     5     rotate right AC
rrl     00011111     5     rotate right AC,CY/L
halt     00000000     8     Pulse 'H' (doesn't stop the CPU)
ccl     00000010     5     CY/L := 0
scl     00000011     5     CY/L := 1
dint     00000100     6     IEN := 0
ien     00000101     6     IEN := 1
csa     00000110     5     AC := S
cas     00000111     6     S := AC (not SA or SB)
nop     00001000     5     no operation

'''

import threading
from emupy.emu import setaddressbus

class chip_8060(threading.Thread):
    def __init__(self, threadID, name, 
                 nwds, nrds, nenin, nenout, nbreq, nhold, nrst, cont,
                 db7, db6, db5, db4, db3, db2, db1, db0,
                 sense_a, sense_b, flag_0, gnd, vcc, nads, xout, xin,
                 ad11, ad10, ad9, ad8, ad7, ad6, ad5, ad4, ad3, ad2, ad1, ad0,
                 sin, sout, flag_2, flag_1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        print "Initialising " + self.name
        self.db0 = db0
        self.db1 = db1
        self.db2 = db2
        self.db3 = db3
        self.db4 = db4
        self.db5 = db5
        self.db6 = db6
        self.db7 = db7
        self.ad0 = ad0
        self.ad1 = ad1
        self.ad2 = ad2
        self.ad3 = ad3
        self.ad4 = ad4
        self.ad5 = ad5
        self.ad6 = ad6
        self.ad7 = ad7
        self.ad8 = ad8
        self.ad9 = ad9
        self.ad10 = ad10
        self.ad11 = ad11
        self.nwds = nwds
        self.nrds = nrds
        self.nenin = nenin 
        self.nenout = nenout 
        self.nbreq = nbreq
        self.nhold = nhold
        self.nrst = nrst
        self.cont = cont
        self.sense_a = sense_a
        self.sense_b = sense_b
        self.flag_0 = flag_0
        self.nads = nads
        self.xout = xout
        self.xin = xin # Clock in
        self.sin = sin # Clock out
        self.sout = sout
        self.flag_2 = flag_2
        self.flag_1 = flag_1
        self.pc = 0x00 # Program Counter (16-bit)
        self.p0 = 0x00 # Pointer Register 0 (16-bit)  
        self.p1 = 0x00 # Pointer Register 1 (16-bit)
        self.p2 = 0x00 # Pointer Register 2 (16-bit)
        self.p3 = 0x00 # Pointer Register 3 (16-bit)
        self.ac = 0x00 # Accumulator (8-bit)
        self.er = 0x00 # Extension Register (Bits?)
        self.sr = 0x00 # Status Register (Bits?)
        self.ir = 0x00 # Instruction Register (8-bit)
        self.ior = 0x00 # IO Register (8-Bits?)
        self.ar = 0x00 # Address Register (16-bit)
        self.current_xin = 0
        
        # Instruction dictionary
        
        self.instructions = {
                             0x00: [],
                             0x01: [],
                             0x02: [],
                             0x08: [3, 11, self.instr_nop], # and so on...
                             
                             
                             0xc0: [3, 11, self.instr_ld], # 3 Cycles, 11 Microcycles, Function "instr_Ld"
                             0xc1: [3, 9, self.instr_st],
                             0xc2: [3, 9, self.instr_st],
                             0xc3: [3, 9, self.instr_st],
                             0xc4: [3, 9, self.instr_st],
                             0xc5: [3, 9, self.instr_st],
                             0xc6: [3, 9, self.instr_st],
                             0xc7: [3, 9, self.instr_st],
                             0xc8: [3, 9, self.instr_st], # 3 Cycles, 9 Microcycles, Function "instr_st"
                             0xc9: [3, 9, self.instr_st],
                             0xca: [3, 9, self.instr_st],
                             0xcb: [3, 9, self.instr_st],
                             0xcc: [3, 9, self.instr_st],
                             0xcd: [3, 9, self.instr_st],
                             0xce: [3, 9, self.instr_st],
                             0xcf: [3, 9, self.instr_st],
                             
                             }        
    
    def run(self):
        from emupy.components.bus_unit import bus
        from emupy.emu import decodebus
        print "Starting " + self.name
        print "Waiting for first clock pulse..."
        self.wait_cycle(1)
        while True:
            instruction = decodebus(int(bus[self.db0]),int(bus[self.db1]),int(bus[self.db2]),int(bus[self.db3]),int(bus[self.db4]),int(bus[self.db5]),int(bus[self.db6]),int(bus[self.db7]))
            #print "Instruction on bus: " + str(instruction)
            self.wait_cycle(self.instructions[instruction][0])
            self.instructions[instruction][2]()
            setaddressbus(self.pc)
            # set address bus to value in program counter.
    
    def instr_nop(self):
        #print ("NOP")
        # Or self.pc.inc if we create these registers as their own type
        self.pc = self.pc + 1
        if self.pc == 4096:
            self.pc = 0
    
    def instr_ld(self):
        pass
    
    def instr_st(self):
        pass
    
    def wait_cycle(self, cycles):
        from emupy.components.bus_unit import bus
        for n in range(0,cycles):
            while bus[self.xin] == self.current_xin:
                pass
            self.current_xin = bus[self.xin]
            #while bus[self.xin == self.current_xin]:
            #    pass
            #self.current_xin = self.xin