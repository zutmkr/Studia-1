
class Ksztalt():
    def __init__(self, ile_katow):
        self.ile_katow = ile_katow

class Rozmiar():
    def __init__(self, bok):
        self.bok = bok

class Kwadrat(Ksztalt,Rozmiar):
    def __init__(self):
        Rozmiar.bok = int(input('Podaj dlugosc boku kwadratu: '))

    def zmien_rozmiar(self, mnoznik):
        self.bok *= mnoznik
        print('Kwadrat ma teraz rozmiar ', self.bok)

class Kolo(Ksztalt,Rozmiar):
    def __init__(self):
        self.bok = int(input('Podaj srednice kola: '))

    def zmien_rozmiar(self,mnoznik):
        self.bok *= mnoznik
        print('Kolo ma teraz srednice ', self.bok)


x = Kwadrat()
x.zmien_rozmiar(int(input('Podaj mnoznik:')))


y = Kolo()
y.zmien_rozmiar(int(input('Podaj mnoznik:')))
