'''SLIDE 22 ZADATAK 1

Definirajte klasu Zaposlenik s atributima ime, prezime i plaća.
Dodajte metodu prikazi_podatke koja ispisuje sve podatke o zaposleniku.
Zatim definirajte podklasu Menadžer koja nasljeđuje Zaposlenik i dodaje
atribut odjel. Nadjačajte metodu prikazi_podatke u Menadžer klasi kako bi
ispisivala sve podatke, uključujući odjel.

'''
class Zaposlenik:
    def __init__(self, ime, prezime, placa):
        self.ime = ime
        self.prezime = prezime
        self.placa = placa
    def prikazi_podatke(self):
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Plaća: {self.placa}")
    
class Menadzer(Zaposlenik):
    def __init__(self, ime, prezime, placa, odjel):
        super().__init__(ime, prezime, placa)
        self.odjel = odjel
    def prikazi_podatke(self):
        super().prikazi_podatke()
        print(f"Odjel: {self.odjel}")

zaposlenik = Zaposlenik("Ivo", "Ivić", 1500)
print("Podaci o zaposleniku:")
zaposlenik.prikazi_podatke()

print("\nPodaci o menadžeru:")
menadzer = Menadzer("Marko", "Markić", 2600, "Prodaja")
menadzer.prikazi_podatke()