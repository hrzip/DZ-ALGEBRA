# Ispišite brojeve od 0 do 9 (uključivo) te od 9 do 0 (uključivo)
for broj in range (0, 10, 1):
    print(broj)

print('\n')

for broj in range (9, -1, -1):
    print(broj)

print('\n')
# Ispišite parne brojeve od 0 do 20, u jednom retku sa zarezom između svakog broja.

for parni_broj in range (0, 22, 2):
    if parni_broj == 20:   #dodao sam ovo jer me živcirao zarez nakon broj 20 ako sam stavio samo zarez kao end, a ako sam stavio end bez ičega i zarez kao sep u istu liniju zarezi se nisu vidjeli.
        print(parni_broj, end="")
    else:
        print(parni_broj, end=",")
print('\n')
# Ispišite kvadrate brojeva od 1 do 5.

for broj_za_kvadriranje in range(1, 6):
    kvadrat = broj_za_kvadriranje ** 2
    print(f"Kvadrat broja {broj_za_kvadriranje} je {kvadrat}")
print('\n')
# Ispišite zbroj brojeva od 1 do 10.
zbroj=0
for broj_za_zbrajanje in range(1, 11):
    zbroj += broj_za_zbrajanje
    print(f"Zbroj broja {broj_za_zbrajanje} je {zbroj}")
print('\n')
# Ispišite svaki drugi broj od 1 do 15.

for broj in range (1, 16, 2):
    print(broj)

print('\n')
# Ispišite tablicu množenja za broj 5 do 10.

glavni_broj = 5
print(f"Tablica množenja za broj {glavni_broj}:")

for broj_za_mnozenje in range(1, 11):
    rezultat = glavni_broj * broj_za_mnozenje
    print(f"{glavni_broj} × {broj_za_mnozenje} = {rezultat}")

print('\n')
# Ispišite brojeve od 0 do 100 s korakom od 10.

for broj in range (0, 110, 10):
    print(broj)

print('\n')
'''Kreirati aplikaciju koja će u konzolu iscrtati bor kao na slici ispod.
Korisnik treba unijeti visinu bora i znak. Primjer ispisa bora za visinu 7 i znak „*":'''

visina = int(input("Visina bora: "))
znak = input("Znak: ")

for i in range(visina):
    broj_razmaka = visina - i - 1 #ovo sam zamislio kao da ono što upiše korisnik da bude koliko će biti razmaka, ali od 0 do minus jedan od unešenog iznosa.
    
    print(" " * broj_razmaka + znak)

razmak_debla = visina // 2 - 1  #ovdje sam podijelio što je upisano za visinu i samo još -1 jer inače se ne bi deblo micalo skupa sa borom nego bi ostalo lijevo
print(" " * razmak_debla + "|||")