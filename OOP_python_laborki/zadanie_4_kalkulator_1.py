class Zliczanie:
    wynik = 0
    def __init__(self, a, b):
        self.a=int(a)
        self.b=int(b)
        z = input('Chcesz dodac? ')
        if z=='t':
            Zliczanie.wynik = self.a+self.b
        else:
            Zliczanie.wynik = self.a-self.b
    def dodawanie(self,a,b):
        return self.a + self.b

    def odejmowanie(self,a,b):
        return self.a - self.b

a = input("Podaj liczbe:")
b = input("Podaj liczbe:")
print(a, "i", b)
odpal = Zliczanie(a,b)
print("Dodawanie ",odpal.dodawanie(a,b))
print("Odejmowanie ",odpal.odejmowanie(a,b))
print("Wynik z konstruktora ", Zliczanie.wynik)
print("Wynik z obiektu ", odpal.wynik)

odpal.wynik += odpal.wynik
print("Wynik z konstruktora ", Zliczanie.wynik)
print("Wynik z obiektu ", odpal.wynik)