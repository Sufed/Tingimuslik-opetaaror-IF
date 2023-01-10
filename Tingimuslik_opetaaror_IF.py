from math import *
from random import *
#Harjutus 8.
piim_hind = 2.50
saia_hind = 3.00
leiba_hind = 4.00

tooted = []
#Спросить хочет ли купить.
piim = input("Kas soovid piima osta (jaj või ei)? ")
if piim == "jah":
    tooted += ["piim"]
#Спросить хочет ли купить.
saia = input("Kas soovid leiba osta (jah või ei)? ")
if saia == "jah":
    tooted += ["saia"]
#Спросить хочет ли купить.
leiba = input("Kas soovid mune osta (jah või ei)? ")
if leiba == "jah":
    tooted += ["leiba"]
#Вычисляем цену.
kogu_hind = 0
if "piim" in tooted:
    kogu_hind += piim_hind
if "saia" in tooted:
    kogu_hind += saia_hind
if "leiba" in tooted:
    kogu_hind += leiba_hind
print("Sa ostate:", tooted)
print(f"Koguhind: {kogu_hind}")
print()
print()
print()
#Harjutus 7.
print("Harjutus 7.)
while True:
    try:
        pikkus = float(input("Mis on sinu pikkus? "))
        if pikkus > 0:
            break
        print("Pikkus peab olema suurem kui 0.")
    except ValueError:
        print("On vaja arvude tüüp kasutada.")
sugu = input("Mis sugu sa oled? ")
if sugu.lower() == "mees":
    if pikkus < 1.7:
        print("Oled lühike mees.")
    elif pikkus < 1.8:
        print("Oled keskmise pikkusega mees.")
    else:
        print("Oled pikk mees.")
elif sugu.lower() == "naine":
    if pikkus < 1.6:
        print("Oled lühike naine.")
    elif pikkus < 1.7:
        print("Oled keskmise pikkusega naine.")
    else:
        print("Oled pikk naine.")
else:
    print("Sugu on tundmatu.")
#Harjutus 6.
print("Harjutus 6.)
while True:
    try:
        pikkus = float(input("Mis on sinu pikkus? "))
        if pikkus > 0:
            break
        print("Pikkus peab olema suurem kui 0.")
    except ValueError:
        print("On vaja arvude tüüp kasutada.")
if pikkus < 1.5:
    print("Oled lühike.")
elif pikkus < 1.8:
    print("Oled keskmise pikkusega.")
else:
    print("Oled pikk.")
print()
print()
print()
#Harjutus 5.
print("Harjutus 5.)
while True:
    try:
        temperatuur = float(input("Kui külm on väljas? "))
        if temperatuur >= 0:
            break
        print("Temperatuur peab olema suurem või võrdne 0.")
    except ValueError:
        print("On vaja arvude tüüp kasutada.")
if temperatuur > 18:
    print("Soovitame kandma soojemaid riideid.")
else:
    print("Soovitame kandma jopet või särki.")
print()
print()
print()
#Harjutus 4.
print("Harjutus 4.)
while True:
    try:
        hind = float(input("Kui palju maksab toode? "))
        if hind > 0:
            break
        print("Hind peab olema suurem kui 0.")
    except ValueError:
        print("On vaja arvude tüüp kasutada.")
if hind > 700:
    hind *= 0.7
print(f"Lõpphind on {hind} eurot.")
print()
print()
print()
#Harjutus 3.
print("Harjutus 3.)
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
    if (nimi1.lower() == "kadurin" and nimi2.lower() == "grüntal") or (nimi1.lower() == "grüntal" and nimi2.lower() == "kadurin"):
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
