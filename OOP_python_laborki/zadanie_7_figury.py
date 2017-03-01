class FiguraGeometryczna():
    nazwa = ""
    polozenie = []

    def __init__(self):
        self.nazwa = input("Podaj nazwe figury: ")
        wierzcholek = int(input("Ile wierzcholkow?: "))

        for i in range(wierzcholek):
            x = int(input("Podaj x: "))
            y = int(input("Podaj y: "))
            z = int(input("Podaj z: "))
            self.polozenie.append([x, y, z])

    def pokaz(self):
        s = "Nazwa: " + self.nazwa + "\nLiczba wierzcholkow: " + str(len(self.polozenie)) + "\nWierzcholki:\n"
        for i in range(len(self.polozenie)):
            s += str(self.polozenie[i]) + "\n"
        print(s)


fig = FiguraGeometryczna()
fig.pokaz()