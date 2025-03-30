# Izračunajte prosječno trajanje filmova u listi koju ste odabrali
lista_filmova = ["Gospodar Prstenova", "Hachiko", "Pink Panther", "Zvjezdani ratovi", "All Quiet on the Western Front"]
trajanje_filmova_u_minutama = [178, 93, 93, 121, 147]

prosjecno_trajanje = sum(trajanje_filmova_u_minutama) / len(lista_filmova)

print(f"Popis filmova: {lista_filmova}")
print()
print(f"Prosječno trajanje filmova je: {prosjecno_trajanje}")
