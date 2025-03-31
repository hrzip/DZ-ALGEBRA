# Napravite listu s pet različitih žanrova filmova i ispišite ih na ekran. Zatim, uradite drugu listu koja sadrži pet filmova, pri čemu svaki film pripada jednom od žanrova iz prve liste

zanrovi = ["avantura", "obiteljski", "komedija", "SF", "ratni"]
print(zanrovi)
lista_filmova = ["Gospodar Prstenova", "Hachiko", "Pink Panther", "Zvjezdani ratovi", "All Quiet on the Western Front"]

nova_lista = []

for i in range(len(zanrovi)):
    zanr = zanrovi[i]
    film = lista_filmova[i]
    nova_lista.append([film, zanr])

for stavka in nova_lista:
    print(f"{stavka[0]} spada u žanr \"{stavka[1]}\"")



