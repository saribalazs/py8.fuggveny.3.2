'''
3.2 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!

Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! 
Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!
'''
def harommal_oszthatok(*args):
    num = 0
    for i in lista:
        if i % 3 == 0:
            num += 1
    return num

lista = []
for i in range(10):
    szam = int(input("Kérem adjon meg egy számot!"))
    lista.append(szam)

print(harommal_oszthatok(lista))