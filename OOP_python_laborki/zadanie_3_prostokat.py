
class Prostokat:
    def __init__(self, bokA, bokB):
        self.bokA = bokA
        self.bokB = bokB

    def pole(self):
        self.wynik = self.bokA*self.bokB
        return self.wynik

p_1 = Prostokat(3,2)
#print(p_1.bokA)
#print("Pole 1 prostokata ", p_1.pole())
        
p_2 = Prostokat(12,1)
#print(p_2.bokA)
#print("Pole 2 prostokata ", p_2.pole())

p_3 = Prostokat(4,8)
#print(p_3.bokA)
#print("Pole 3 prostokata ", p_3.pole())

lista=[p_1,p_2,p_3, Prostokat(4,8)]
for p in lista:
    print("Pola prostokatow:", p.pole())

def zrob(p):
    print("Pole prostokata: ", p.pole())
    print("Boki: ", p.bokA,"," ,p.bokB)

for p in lista:
    zrob(p)

