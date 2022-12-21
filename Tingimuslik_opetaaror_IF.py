from math import *
from random import *
#Harjutus 3.
while True:
        try:
            a=float(input("Pikkus: "))
            if a>0: break
        except:
            print("On vaja arvude tüüp kasutada, mis on suurem kui 0")
while True:
        try:
            b=float(input("Pikkus: "))
            if b>0: break
        except:
            print("On vaja arvude tüüp kasutada, mis on suurem kui 0")
while True:
    v=input("Kas tahad remoti teha? ")
    if v.upper()=="JAH" or v.upper()=="EI" : break
if v.upper()=="JAH":
    while True:
        try:
            hind=float(input("Kui palju maksab m^2"))
            break
        except TypeError:
            print()
    hind=a*b*hind
    print(hind)
else:
    print("Fuck you")
#Harjutus 2.
print("Harjutus 2.")
while True:
    nimi1=input("Mis sul nimi on? ") #Kadurin
    if nimi1.isalpha(): break
while True:
    nimi2=input("Mis sul nimi on? ") #Grüntal
    if nimi2.isalpha(): break
    if nimi1.lower()==("Kadurin") and nimi2.lower()==("Grüntal"):
        print("Täna istume meie pingil.")
    else:
        print("Vale andetüüp.")
print()
print()
print()
#Harjutus 1.
print("Harjutus 1.")
while True:
    nimi=input("Mis sul nimi on? ")
    if nimi.isalpha(): break
if nimi.upper==("JUKU") and nimi.isdigit:
    while True:
        try:
            vanus=int(input("Kui vana sa oled? "))
            break
        except:
            print("On vaja arvude tüüp kasutada")
    if 0<vanus<6:
        print("Pilet on tasuta.")
    elif 6<=vanus<=14:
        print("Lapse pilet.")
    elif 15<=vanus<65:
        print("Täispilet")
    elif 65<=vanus<100:
        print("Sooduspilet")
    else:
        print("Vanus ei sobi.")
else:
    print("Ma ostsin Juku")