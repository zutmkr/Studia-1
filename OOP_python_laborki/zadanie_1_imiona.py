class ImionaNazwiska:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

osobaA = ImionaNazwiska("Anna" , "Nowak")
print(osobaA.imie, osobaA.nazwisko)

osobaB = ImionaNazwiska("Ola" , "Kowalska")
print(osobaB.imie, osobaB.nazwisko)

osobaC = ImionaNazwiska("ALa" , "Iksinska")
print(osobaC.imie, osobaC.nazwisko)
