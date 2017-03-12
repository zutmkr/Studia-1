from time import sleep
import random
import os

stuff = ['miecz', 'zbroja', 'potion', 'buty', 'kusza', 'tiara', 'pierscien', 'amulet', 'tarcza', 'pas', 'rekawice',
         'pet']
dobry_prefix = ['dobre', 'magiczne', 'legendarne', 'rzadkie']
zly_prefix = ['znoszone', 'przeklete', 'zepsute', 'nawiedzone']
rodzaj_mapy = [[0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
prawda_falsz = [True, False]


class Przedmiot:
    def __init__(self):
        self.nazwa = random.choice(stuff)


class Pokoj:
    otwarty = True
    loot = Przedmiot()
    droga = False


class Mapa():
    def __init__(self):
        # tworzenie mapy gry
        wielkosc_mapy = random.choice(rodzaj_mapy)
        self.mapa = []
        for i in range(len(wielkosc_mapy)): self.mapa.append(wielkosc_mapy[:])
        print(len(wielkosc_mapy))
        self.lista_pokoi = [Pokoj() for i in range(len(wielkosc_mapy) ** 2)]
        k = 0
        for i in range(len(wielkosc_mapy)):
            for j in range(len(wielkosc_mapy)):
                self.mapa[i][j] = self.lista_pokoi[k]
                if random.choice(prawda_falsz):
                    self.mapa[i][j].otwarty = True
                else:
                    self.mapa[i][j].otwarty = False
                k += 1

    def PrzygotujMape(self):
        if len(self.mapa[0]) == 3:
            self.mapa[1][0].otwarty = True
            self.mapa[1][1].otwarty = True
            self.mapa[1][2].otwarty = True
            self.mapa[2][2].otwarty = True
        elif len(self.mapa[0]) == 5:
            self.mapa[1][0].otwarty = True
            self.mapa[1][1].otwarty = True
            self.mapa[1][2].otwarty = True
            self.mapa[2][2].otwarty = True
            self.mapa[2][3].otwarty = True
            self.mapa[3][3].otwarty = True
            self.mapa[3][4].otwarty = True
            self.mapa[4][4].otwarty = True
        elif len(self.mapa[0]) == 7:
            self.mapa[1][0].otwarty = True
            self.mapa[1][1].otwarty = True
            self.mapa[2][1].otwarty = True
            self.mapa[3][1].otwarty = True
            self.mapa[3][2].otwarty = True
            self.mapa[4][2].otwarty = True
            self.mapa[5][2].otwarty = True
            self.mapa[2][2].otwarty = True
            self.mapa[2][3].otwarty = True
            self.mapa[2][4].otwarty = True
            self.mapa[3][4].otwarty = True
            self.mapa[5][3].otwarty = True
            self.mapa[6][3].otwarty = True
            self.mapa[6][4].otwarty = True
            self.mapa[6][5].otwarty = True
            self.mapa[6][6].otwarty = True

    def RysujMape(self):
        os.system('cls')  # czyszczenie ekranu
        LOGO()
        for i in range(len(self.mapa[0])):
            for j in range(len(self.mapa[0])):
                try:
                    if self.mapa[i][j].otwarty:
                        if j == len(self.mapa[0]) - 1:
                            print('_')
                        else:
                            print('_', end='')
                    else:
                        if j == len(self.mapa[0]) - 1:
                            print('#')
                        else:
                            print('#', end='')
                except:
                    if j == len(self.mapa[0]) - 1:
                        print('8')
                    else:
                        print('8', end='')


class Wartosciowy(Przedmiot):
    def dodaj_przedmiot(self):
        z = random.choice(dobry_prefix)
        y = Przedmiot()
        z = z + ' ' + y.nazwa
        y.nazwa = z
        return y


class Smiec(Przedmiot):
    def dodaj_przedmiot(self):
        z = random.choice(zly_prefix)
        y = Przedmiot()
        z = z + ' ' + y.nazwa
        y.nazwa = z
        return y


class Gracz():
    lista = []
    punkty = 0
    pozycja = []

    def pokaz_plecak(self):
        for Przedmiot in self.lista:
            print(Przedmiot.nazwa)

    def pobierzPozycje(self, Maps):
        for i in range(len(Maps.mapa)):
            try:
                if (Maps.mapa[i].index(self) >= 0):
                    self.pozycja = []
                    self.pozycja.append(i)
                    self.pozycja.append(Maps.mapa[i].index(self))
            except:
                continue

    def Dodaj_do_Plecak(self):
        if random.choice(prawda_falsz):
            self.lista.append(Wartosciowy().dodaj_przedmiot())
            self.punkty += 1
        else:
            self.lista.append(Smiec().dodaj_przedmiot())
            self.punkty -= 1


def PoruszaniePoMapie(gr, Maps):
    gr.pobierzPozycje(Maps)

    def Sciana(t):
        print('Nie mozesz tam isc, to sciana.')
        sleep(t)

    def Stala_pozycja(gr, Maps):
        Maps.mapa[gr.pozycja[0]][gr.pozycja[1]] = Pokoj()
        gr.pobierzPozycje(Maps)
        gr.Dodaj_do_Plecak()

    def W(gr, Maps):
        if gr.pozycja[0] - 1 >= 0 and Maps.mapa[gr.pozycja[0] - 1][gr.pozycja[1]].otwarty:
            Maps.mapa[gr.pozycja[0] - 1][gr.pozycja[1]] = gr
            Stala_pozycja(gr, Maps)
        else:
            Sciana(2)

    def S(gr, Maps):
        if gr.pozycja[0] + 1 < len(Maps.mapa) and Maps.mapa[gr.pozycja[0] + 1][gr.pozycja[1]].otwarty:
            Maps.mapa[gr.pozycja[0] + 1][gr.pozycja[1]] = gr
        else:
            Sciana(2)

    def A(gr, Maps):
        if gr.pozycja[1] - 1 >= 0 and Maps.mapa[gr.pozycja[0]][gr.pozycja[1] - 1].otwarty:
            Maps.mapa[gr.pozycja[0]][gr.pozycja[1] - 1] = gr
            Stala_pozycja(gr, Maps)
        else:
            Sciana(2)

    def D(gr, Maps):
        if gr.pozycja[1] + 1 < len(Maps.mapa) and Maps.mapa[gr.pozycja[0]][gr.pozycja[1] + 1].otwarty:
            Maps.mapa[gr.pozycja[0]][gr.pozycja[1] + 1] = gr
        else:
            Sciana(2)

    while True:
        print('\n\nQuo vadis?>', end='')
        h = input()
        if h == 'w':
            W(gr, Maps)
        elif h == 's':
            S(gr, Maps)
            if gr.pozycja[0] == len(Maps.mapa) - 1 and gr.pozycja[1] == len(Maps.mapa) - 1:
                print('Wygrales, oto Twoje skarby: ')
                gr.pokaz_plecak()
                print('Zdobyles :', gr.punkty, 'punktow')
                exit(0)
            else:
                Stala_pozycja(gr, Maps)
        elif h == 'a':
            A(gr, Maps)
        elif h == 'd':
            D(gr, Maps)
            if gr.pozycja[0] == len(Maps.mapa) - 1 and gr.pozycja[1] == len(Maps.mapa) - 1:
                print('Wygrales, oto Twoje skarby: ')
                gr.pokaz_plecak()
                print('Zdobyles :', gr.punkty, 'punktow')
                exit(0)
            else:
                Stala_pozycja(gr, Maps)
        else:
            print('Zla droga kroczysz!')

        Maps.RysujMape()


def LOGO():
    with open('LOGO.txt') as plik:
        print(plik.read())


gr = Gracz()

Maps = Mapa()

Maps.mapa[0][0] = gr

Maps.PrzygotujMape()

Maps.RysujMape()

PoruszaniePoMapie(gr, Maps)
