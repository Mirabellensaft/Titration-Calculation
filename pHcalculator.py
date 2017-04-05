print "Enter concentration of the base in [mol/l]"
cAc = float(raw_input())
print "%r mol/l" % cAc

print "Enter used Volume of the base in [l]"
vAc = float(raw_input())
print "%r l" % vAc

print "Enter Volume of the acid in [l]"
vBa = float(raw_input())
print "%r l" % vBa

print "Calculating the amount of substance [mol] of the base"
print vAc * cAc

print "Calculating the concentration of the acid"
print (vAc * cAc) / vBa

print "pH of the acid"
import math
print - math.log10((vAc * cAc) / vBa)
