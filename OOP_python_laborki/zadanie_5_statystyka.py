import random
import math
from operator import attrgetter

class Statystyka():
    x = 0
    suma =0
    srednia = 0

    def __init__(self):
        self.x = random.randint(1, 100)

    def suma_listy(self, list):
        suma = 0
        for i in range(len(list)):
            suma = list[i].x + suma
            self.suma = suma
        return suma

    def srednia(self, list):
        self.srednia = self.suma_listy(list)/len(list)
        return self.srednia

    def mediana(self, list):
        new_list = sorted(list, key=lambda x: x.x)
        if len(new_list)%2==0:
            a = len(new_list)/2
            a = int(a)
            return (new_list[a].x + new_list[a+1].x)/2
        else:
            return new_list[math.ceil((len(new_list)/2))].x

    def minimum(self, list):
        return min(list, key=lambda x: x.x)

    def maksimum(self, list):
        return max(list, key=attrgetter('x'))


##lista obiekow w tym przypadku dla randomowej ilosci obiektow
list = [Statystyka() for i in range (random.randint(3,20))]
print('wygenerowano ', len(list), ' obiektow o kolejnych wartosciach: ')
for i in range (len(list)):
    print('[', i, '] wartosc x wynosi ', list[i].x)
##suma wartosci obiekow
print('Suma wartosci obiektow listy wynosi: ', list[1].suma_listy(list))

##wartosci atrybutu suma obiektu o indeksie 0 i 1
##print(list[0].suma)
##print(list[1].suma)

print('Srednia wartosci obiektow listy wynosi:', round(list[1].srednia(list),2))
#print('posortowana lista: ')
# new = list[1].mediana(list)
# for i in range (len(new)):
#     print('[', i, '] wartosc x wynosi ', new[i].x)

print('Mediana wynosi :', list[1].mediana(list))

print('Wartosc minimalna obiektow listy wynosi: ', list[1].minimum(list).x)

print('Wartosc maksymalna obiektow listy wynosi : ', list[1].maksimum(list).x)
