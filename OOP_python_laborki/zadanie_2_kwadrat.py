class Kwadrat:
    def __init__(self, bokA):
        self.bokA = bokA

    def pole(self):
        self.wynik = self.bokA**2
        return self.wynik

kwadrat_1 = Kwadrat(3)
#print(kwadrat_1.bokA)
print("Pole 1 kwadratu ", kwadrat_1.pole())
        
kwadrat_2 = Kwadrat(12)
#print(kwadrat_2.bokA)
print("Pole 2 kwadratu ", kwadrat_2.pole())

kwadrat_3 = Kwadrat(4)
#print(kwadrat_3.bokA)
print("Pole 3 kwadratu ", kwadrat_3.pole())
