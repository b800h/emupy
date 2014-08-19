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