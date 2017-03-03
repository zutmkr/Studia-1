import FunkcjeKalendarza
class Kalendarz():
    rok = 0
    miesiac = 0

    def __init__(self,miesiac, rok):
        self.rok = rok
        self.miesiac = miesiac
    def pokaz(self):
        dni_tygodnia = ['nie', 'pon', 'wto', 'sro', 'czw', 'pia', 'sob']

        for i in range(FunkcjeKalendarza.DzienTygodnia(self.rok, self.miesiac), 7):
            print(dni_tygodnia[i],'', end='')
        if FunkcjeKalendarza.DzienTygodnia(self.rok, self.miesiac) > 0:
            for i in range (0, FunkcjeKalendarza.DzienTygodnia(self.rok, self.miesiac)):
                print(dni_tygodnia[i],'', end='')
        print()

        for i in range (1,(1 + FunkcjeKalendarza.DniWMiesiacu(self.miesiac,self.rok))):
            if i%7==0:
                if i in [14,21,28]:
                    print(i, '')
                else:
                    print(i,' ')
            elif i in [3,4,5,6,7]:
                print(i,'  ', end='')
            elif i in [10,11,12,13]:
                print(i, ' ',end='')
            elif i in [2,9]:
                print('',i,'  ', end='')
            else:
                print(i, ' ', end='')

kal = Kalendarz(5,2017)
kal.pokaz()