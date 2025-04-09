'''SLIDE 14 ZADATAK 3

Definirajte klasu Film s atributima naslov, režiser,
godina izdanja i trajanje. Kreirajte konstruktor za inicijalizaciju
ovih atributa. Dodajte metodu prikazi_film koja ispisuje
informacije o filmu.

'''

class Film:
    def __init__(self, naslov, reziser, godina_izdanja, trajanje):
        self.naslov = naslov
        self.reziser = reziser
        self.godina_izdanja = godina_izdanja
        self.trajanje = trajanje
    def prikazi_film(self):
        print(f"Naslov filma: {self.naslov}")
        print(f"Režiser filma: {self.reziser}")
        print(f"Godina izdanja: {self.godina_izdanja}")
        print(f"Trajanje filma: {self.trajanje}")

film = Film("Tibet", "Ivo Ivić", "2017", "168 minuta")
film.prikazi_film()
