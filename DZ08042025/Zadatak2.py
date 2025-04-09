'''SLIDE 22 ZADATAK 2

 Definirajte klasu Vozilo s atributima marka i godina proizvodnje.
Dodajte metodu prikazi_podatke koja ispisuje sve podatke o vozilu. Zatim
definirajte podklasu Kamion koja nasljeđuje Vozilo i dodaje atribut
nosivost. Nadjačajte metodu prikazi_podatke u Kamion klasi kako bi
ispisivala sve podatke, uključujući nosivost.

'''

class Vozilo:
    def __init__(self, marka, godina_proizvodnje):
        self.marka = marka
        self.godina_proizvodnje = godina_proizvodnje
    def prikazi_podatke(self):
        print(f"Marka vozila: {self.marka}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")

class Kamion(Vozilo):
    def __init__(self, marka, godina_proizvodnje, nosivost):
        super().__init__(marka, godina_proizvodnje)
        self.nosivost = nosivost
    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Nosivost: {self.nosivost}")

kamion = Kamion("Iveco", 2019, 1570)
kamion.prikazi_podatke()