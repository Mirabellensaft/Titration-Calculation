# import locale
# locale.setlocale(locale.LC_ALL, 'de_DE')
# print "{0:n}".format(11111.2111)
print "Name the file your values will be saved in"
filename = raw_input(">")
target = open(filename, "w")

name_base = raw_input("Enter name of base: ")
conc_base = float(raw_input("Enter concentration of the base in [mol/l]"))
print "%r mol/l" % conc_base
vol_base = float(raw_input("Enter used Volume of the base in [l]"))
print "%r l" % vol_base
target.write("Substance: %r" % name_base)
target.write("\n")
target.write("Concentration: %d mol/l" % conc_base)
target.write("\n")
target.write("Volume used: %d l" % vol_base)
target.write("\n")

name_acid = raw_input("Enter name of acid: ")
vol_acid = float(raw_input("Enter Volume of the acid in [l]"))
print "%r l" % vol_base

target.write("Substance: %r" % name_acid)
target.write("\n")
target.write("Volume: %d l" % vol_acid)
target.write("\n")

print "Calculating the amount of substance [mol] of the base"
print vol_acid * conc_base
mol_acid = vol_acid * conc_base

target.write("Amount of substance of the acid: %d mol " % mol_acid)
target.write("\n")

print "Calculating the concentration of the acid"
print (vol_base * conc_base) / vol_acid
conc_acid = (vol_base * conc_base) / vol_acid

target.write("Concentration of the acid: %d mol/l" % conc_acid)
target.write("\n")

print "pH of the acid"
import math
print - math.log10((vol_base * conc_base) / vol_acid)
pH_acid = - math.log10((vol_base * conc_base) / vol_acid)

target.write("pH of the acid: %d" % pH_acid)
target.write("\n")

target.close()


# things to add:
# auswahl saure base ehrprotonige sauren basen
# ausgabe in datei schreiben, neue rechnung, neue zeile,
# txt datei so schreiben, dass sie in exel importierbar ist
