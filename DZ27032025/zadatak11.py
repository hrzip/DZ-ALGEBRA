#Napravite listu s naslovima filmova i njihovim glavnim glumcima. Zatim izradite drugu listu koja sadrži samo imena glumaca
lista_filmova = ["Gospodar Prstenova", "Hachiko", "Pink Panther", "Zvjezdani ratovi", "All Quiet on the Western Front"]
glavni_glumci = ["Elijah Wood", "Richard Gere", "Steve Martin", "Mark Hamill", "Felix Kammerer"]


ispis = []

for i in range(len(lista_filmova)):
    filmovi = lista_filmova[i]
    glumci = glavni_glumci[i]
    ispis.append((filmovi, glumci))

print()
for x in ispis:
    print(f"Film: {x[0]}, Glavni glumac: {x[1]}")

print()
print("*" * 103)
print()

print(f"Lista glavnih glumaca: {glavni_glumci}")

print()