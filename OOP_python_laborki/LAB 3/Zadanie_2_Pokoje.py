from msvcrt import getch
from time import sleep
import random
import os

stuff = ['miecz', 'zbroja', 'potion', 'buty', 'kusza', 'tiara', 'pierscien', 'amulet', 'tarcza', 'pas', 'rekawice', 'pet']
dobry_prefix = ['dobre', 'magiczne', 'legendarne', 'rzadkie']
zly_prefix = ['znoszone', 'przeklete', 'zepsute', 'nawiedzone']
rodzaj_mapy = [[0,0,0],[0,0,0,0,0],[0,0,0,0,0,0,0]]
prawda_falsz = [True,False]
class Przedmiot():
    def __init__(self):
        self.nazwa = random.choice(stuff)
class Pokoj():
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
        self.lista_pokoi = [Pokoj() for i in range(len(wielkosc_mapy)**2)]
        k = 0
        for i in range(len(wielkosc_mapy)):
            for j in range(len(wielkosc_mapy)):
                self.mapa[i][j] = self.lista_pokoi[k]
                if random.choice(prawda_falsz):
                    self.mapa[i][j].otwarty = True
                else:
                    self.mapa[i][j].otwarty = False
                k +=1

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
        os.system('cls')  # czyszczenie działa na windowsowej konsoli
        LOGO()
        for i in range (len(self.mapa[0])):
            for j in range(len(self.mapa[0])):
                try:
                    if self.mapa[i][j].otwarty:
                        if j == len(self.mapa[0])-1:
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
                if (Maps.mapa[i].index(self)>= 0):
                    self.pozycja = []
                    self.pozycja.append(i)
                    self.pozycja.append(Maps.mapa[i].index(self))
            except:
                continue


def PoruszaniePoMapie(gr,Maps):
    gr.pobierzPozycje(Maps)
    while True:
        h = ord(getch())
        if h == 119:
            if gr.pozycja[0] - 1 >= 0 and Maps.mapa[gr.pozycja[0]-1][gr.pozycja[1]].otwarty == True:
                Maps.mapa[gr.pozycja[0] - 1][gr.pozycja[1]] = gr
                Maps.mapa[gr.pozycja[0]][gr.pozycja[1]] = Pokoj()
                gr.pobierzPozycje(Maps)
                #print(gr.pozycja[0], gr.pozycja[1])
                if random.choice(prawda_falsz):
                    gr.lista.append(Wartosciowy().dodaj_przedmiot())
                    gr.punkty +=1
                else:
                    gr.lista.append(Smiec().dodaj_przedmiot())
                    gr.punkty -=1
            else:
                print('Nie mozesz tam isc, to sciana.')
        elif h == 115:
            if gr.pozycja[0] + 1 < len(Maps.mapa) and Maps.mapa[gr.pozycja[0]+1][gr.pozycja[1]].otwarty == True:
                Maps.mapa[gr.pozycja[0] + 1][gr.pozycja[1]] = gr
                Maps.mapa[gr.pozycja[0]][gr.pozycja[1]] = Pokoj()
                gr.pobierzPozycje(Maps)
                #print(gr.pozycja[0], gr.pozycja[1])
                if gr.pozycja[0] == len(Maps.mapa)-1 and gr.pozycja[1] == len(Maps.mapa)-1:
                    print('Wygrales, oto Twoje skarby: ')
                    gr.pokaz_plecak()
                    print('Zdobyles :', gr.punkty, 'punktow')
                    exit(0)
                else:
                    if random.choice(prawda_falsz):
                        gr.lista.append(Wartosciowy().dodaj_przedmiot())
                        gr.punkty +=1
                    else:
                        gr.lista.append(Smiec().dodaj_przedmiot())
                        gr.punkty -=1
            else:
                print('Nie mozesz tam isc, to sciana.')
        elif h == 97:
            if gr.pozycja[1] - 1 >= 0 and Maps.mapa[gr.pozycja[0]][gr.pozycja[1]-1].otwarty == True:
                Maps.mapa[gr.pozycja[0]][gr.pozycja[1] - 1] = gr
                Maps.mapa[gr.pozycja[0]][gr.pozycja[1]] = Pokoj()
                gr.pobierzPozycje(Maps)
                #print(gr.pozycja[0], gr.pozycja[1])
                if random.choice(prawda_falsz):
                    gr.lista.append(Wartosciowy().dodaj_przedmiot())
                    gr.punkty +=1
                else:
                    gr.lista.append(Smiec().dodaj_przedmiot())
                    gr.punkty -=1
            else:
                print('Nie mozesz tam isc, to sciana.')
        elif h == 100:
            if gr.pozycja[1] + 1 < len(Maps.mapa) and Maps.mapa[gr.pozycja[0]][gr.pozycja[1]+1].otwarty == True:
                Maps.mapa[gr.pozycja[0]][gr.pozycja[1] + 1] = gr
                Maps.mapa[gr.pozycja[0]][gr.pozycja[1]] = Pokoj()
                gr.pobierzPozycje(Maps)
                #print(gr.pozycja[0], gr.pozycja[1])
                if gr.pozycja[0] == len(Maps.mapa)-1 and gr.pozycja[1] == len(Maps.mapa)-1:
                    print('Wygrales, oto Twoje skarby: ')
                    gr.pokaz_plecak()
                    print('Zdobyles :', gr.punkty, 'punktow')
                    exit(0)
                else:
                    if random.choice(prawda_falsz):
                        gr.lista.append(Wartosciowy().dodaj_przedmiot())
                        gr.punkty +=1
                    else:
                        gr.lista.append(Smiec().dodaj_przedmiot())
                        gr.punkty -=1
            else:
                print('Nie mozesz tam isc, to sciana.')
        else:
            print('Zla droga kroczysz!')
            
				sleep(.300)
        Maps.RysujMape()

def LOGO():
    with open('LOGO.txt') as plik:
        print(plik.read())


gr = Gracz()

Maps = Mapa()

Maps.mapa[0][0] = gr

Maps.PrzygotujMape()

Maps.RysujMape()

PoruszaniePoMapie(gr,Maps)