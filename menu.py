# -*- coding: utf-8 -*-

print "Pozdravljeni! To je dnevni meni restavracije Špageti."

meni = {}

while True:
    ime_jedi = raw_input("Prosimo, vnesite željeno jed: ")
    cena_jedi = raw_input("Prosimo, vnesite ceno za '%s': " % ime_jedi)
    meni[ime_jedi] = cena_jedi

    nova_jed = raw_input("Želite dodati novo jed (da/ne)?")

    if nova_jed == "ne":
        break

print "Meni: %s" % meni

with open("meni.txt", "w+") as meni_file:
    for jed in meni:
        meni_file.write("%s, %s EUR\n" % (jed, meni[jed]))

print "Hvala, nasvidenje!"