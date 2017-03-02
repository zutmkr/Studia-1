import os

def Rysuj_Menu():
    print('\t\t KONWERTER')
    print('\t[1]: -- Zamien CALE na CENTYMETRY')
    print('\t[2]: -- Zamien CENTYMETRY na CALE')
    print('\t[3]: -- Zamien KILOGRAMY na FUNTY')
    print('\t[4]: -- Zamien FUNTY na KILOGRAMY')
    print('\t[0]: -- Zakoncz program!')

def Start():
    while 1:
        Rysuj_Menu()
        wybor = input('Wybierz opcję :')
        if wybor == '1':
            cale = float(input('Podaj liczbe do przeliczenia: '))
            print(Konwerter().CaleNaCM(cale), ' centymetrow')
            input('Nacisnij dowolny klawisz by powrocic do menu ')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '2':
            cm = float(input('Podaj liczbe do przeliczenia: '))
            print(Konwerter().CMNaCale(cm), ' cali')
            input('Nacisnij dowolny klawisz by powrocic do menu ')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '3':
            kg = float(input('Podaj liczbe do przeliczenia: '))
            print(Konwerter().KGnaFunty(kg), ' funtow')
            input('Nacisnij dowolny klawisz by powrocic do menu ')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '4':
            funty = float(input('Podaj liczbe do przeliczenia: '))
            print(Konwerter().FuntynaKG(funty), ' kilogramow')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '0':
            exit()


class Konwerter():

    def CaleNaCM(self, cale):
        return (cale * 2.54)

    def CMNaCale(self,cm):
        return (cm * 0.393700787)

    def KGnaFunty(self,kg):
        return (kg * 2.20462262)

    def FuntynaKG(self,funty):
        return (funty * 0.45359237)

Start()