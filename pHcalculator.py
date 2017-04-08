# import locale
# locale.setlocale(locale.LC_ALL, 'de_DE')
# print "{0:n}".format(11111.2111)
import math

filename = raw_input("Name the file your values will be saved in:")
target = open(filename, "w")

name_base = raw_input("Enter name of base: ")
conc_base = float(raw_input("Enter concentration of the base in [mol/l]"))
print "%r mol/l" % conc_base
vol_base = float(raw_input("Enter used Volume of the base in [l]"))
print "%r l" % vol_base
target.write("Substance: %r\n" % name_base)
target.write("Concentration: %s mol/l\n" % conc_base)
target.write("Volume used: %s l\n" % vol_base)

name_acid = raw_input("Enter name of acid: ")
vol_acid = float(raw_input("Enter Volume of the acid in [l]"))
print "%r l" % vol_base

target.write("Substance: %r\n" % name_acid)
target.write("Volume: %s l\n" % vol_acid)

print "Calculating the amount of substance [mol] of the base"
print vol_acid * conc_base
mol_base = vol_acid * conc_base
print "Amount of substance of the base: %s mol." % mol_base

target.write("Amount of substance of the acid: %s mol\n " % mol_acid)

conc_acid = mol_base / vol_acid
print "Concentration of the acid: %s mol/l" % conc_acid

target.write("Concentration of the acid: %s mol/l\n" % conc_acid)

pH_acid = - math.log10(mol_base / vol_acid)
print "pH of the acid: %s" % pH_acid
target.write("pH of the acid: %s\n" % pH_acid)

target.close()


# things to add:
# auswahl saure base ehrprotonige sauren basen
# ausgabe in datei schreiben, neue rechnung, neue zeile,
# txt datei so schreiben, dass sie in exel importierbar ist
