# Napravite dvije liste s naslovima filmova i njihovim godinama izlaska. Zatim spojite te dvije liste u jednu listu tako da svaki element bude niz koji sadrži naziv filma i godinu izlaska

naslov_filma = ["Gospodar Prstenova", "Hachiko", "Hobit", "All Quiet on the Western Front"]
godina_izlaska = [2001, 2009, 2012, 2022]

ispis_stavki = []

for indeks in range(len(naslov_filma)):
    film = naslov_filma[indeks]
    godina = godina_izlaska[indeks]
    ispis_stavki.append([film, godina])

for stavka in ispis_stavki:
    print(f"{stavka[0]} - {stavka[1]}")
    


