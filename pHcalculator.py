print "Enter concentration of acid in [mol/l]"
cAc= float(raw_input())
print "%r mol/l" % cAc

print "Enter used Volume of acid in [l]"
vAc = float(raw_input())
print "%r l" % vAc

print "Enter Volume of base in [l]"
vBa = float(raw_input())
print "%r l" % vBa

print "Calculating the amount of substance [mol] of the acid"
print vAc * cAc

print "Calculating the concentration of the Base"
print (vAc * cAc) / vBa
