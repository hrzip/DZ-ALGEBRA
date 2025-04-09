'''SLIDE 22 ZADATAK 3

Definirajte klasu Knjiga s atributima naslov i autor. Dodajte
metodu prikazi_podatke koja ispisuje sve podatke o knjizi. Zatim definirajte
podklasu Eknjiga koja nasljeđuje Knjiga i dodaje atribut veličina datoteke.
Nadjačajte metodu prikazi_podatke u Eknjiga klasi kako bi ispisivala sve
podatke, uključujući veličinu datoteke

'''

class Knjiga:
    def __init__(self, naslov, autor):
        self.naslov = naslov
        self.autor = autor
    def prikazi_podatke(self):
        print(f"Naslov knjige: {self.naslov}")
        print(f"Autor knjige: {self.autor}")

class Eknjiga(Knjiga):
    def __init__(self, naslov, autor, velicina_datoteke):
        super().__init__(naslov, autor)
        self.velicina_datoteke = velicina_datoteke
    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Veličina datoteke: {self.velicina_datoteke}")

eknjiga = Eknjiga("Divlji Konj", "Ivo ivić", "1024MB")
eknjiga.prikazi_podatke()
