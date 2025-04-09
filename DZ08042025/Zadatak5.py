'''SLIDE 14 ZADATAK 4

Definirajte klasu Računalo s atributima marka,
model, procesor, RAM i HDD. Kreirajte konstruktor za
inicijalizaciju ovih atributa. Dodajte metodu prikazi_racunalo
koja ispisuje sve podatke o računalu.

'''

class Racunalo:
    def __init__(self, marka, model, procesor, ram, hdd):
        self.marka = marka
        self.model = model
        self.procesor = procesor
        self.ram = ram
        self.hdd = hdd
    def prikazi_racunalo(self):
        print(f"Marka računala: {self.marka}")
        print(f"Model računala: {self.model}")
        print(f"Procesor: {self.procesor}")
        print(f"Količina rama: {self.ram}")
        print(f"HDD kapacitet: {self.hdd}")

racunalo = Racunalo("Dell", "rv01b", "Intel i7", "16GB", "1TB" )
racunalo.prikazi_racunalo()