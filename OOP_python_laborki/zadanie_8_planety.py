import os

jedn_astr = 149597870700
float(jedn_astr)

def Wszystkie_Planety(planety):
    for i in range(len(planety)):
        print(planety[i].nazwa)
        print(((float(planety[i].odleglosc_astro)* jedn_astr))/1000, 'tys. km')
        print(planety[i].czy_planeta)

def Rzeczywiste_Planety(planety, zwroc_liste):
    if zwroc_liste:
        new_list = []
        for i in range(len(planety)):
            if planety[i].czy_planeta == 'True':
                new_list.append(planety[i].nazwa)
        return new_list
    else:
        print('Lista planet rzeczywistych: ')
        for i in range(len(planety)):
            if planety[i].czy_planeta == 'True':
                print(planety[i].nazwa)

def Nierzeczywiste_Planety(planety, zwroc_liste):
    if zwroc_liste:
        new_list = []
        for i in range(len(planety)):
            if planety[i].czy_planeta == 'False':
                new_list.append(planety[i].nazwa)
        return new_list
    else:
        print('Lista planet nierzeczywistych: ')
        for i in range(len(planety)):
            if planety[i].czy_planeta == 'False':
                print(planety[i].nazwa)

def Rysuj_Menu():
    print('\t\t CENTRUM ZARZADZANIA PLANETAMI')
    print('\t[1]: -- Wypisz wszystkie planety')
    print('\t[2]: -- Wypisz rzeczyswiste planety')
    print('\t[3]: -- Wypisz nierzeczyswiste planety')
    print('\t[4]: -- Zapisz plik z lista planet pod wybrana nazwa')
    print('\t[0]: -- Zakoncz program!')

def Zapis(planety):
    os.system('cls')
    Rysuj_Menu()
    print('\t |')
    print('\t ----->')
    print('\t\t[1] -- Zapis listy rzeczywistych planet do pliku.')
    print('\t\t[2] -- Zapis listy nierzeczywistych planet do pliku.')
    print('\t\t[Dowolny inny klawisz] -- Cofnij do poprzedniego Menu.')

    x = input('Twoj wybor: ')

    if x == '1':
        planety_r = Rzeczywiste_Planety(planety,1)
        file_name = input('Podaj nazwe pliku: ')
        with open((file_name + '.txt'), 'w') as file:
            for i in range(len(planety_r)):
                file.write(planety_r[i] + '\n')

    elif x == '2':
        planety_r = Nierzeczywiste_Planety(planety,1)
        file_name = input('Podaj nazwe pliku: ')
        with open((file_name + '.txt'), 'w') as file:
            for i in range(len(planety_r)):
                file.write(planety_r[i] + '\n')

    else:
        return


def Start():
    with open('Planety.txt') as plik:
        lista = plik.readlines()

    lista = [x.strip() for x in lista]
    planety = [Planety() for i in range(11)]

    j = 0
    for i in range(len(lista)):
        if i % 3 == 0:
            planety[j].nazwa = lista[i]
            planety[j].odleglosc_astro = lista[i + 1]
            planety[j].czy_planeta = lista[i + 2]
            j = j + 1
    if input('Czy Pluton ma byc traktowany jako planeta ?: ') == 't':
        planety[10].czy_planeta = 'True'
    else:
        planety[10].czy_planeta = 'False'
    os.system('cls')  # czyszczenie działa na windowsowej konsoli

    while 1:
        Rysuj_Menu()
        wybor = input('Wybierz opcję :')
        if wybor == '1':
            Wszystkie_Planety(planety)
            input('Nacisnij dowolny klawisz by powrocic do menu ')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '2':
            Rzeczywiste_Planety(planety,0)
            input('Nacisnij dowolny klawisz by powrocic do menu ')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '3':
            Nierzeczywiste_Planety(planety,0)
            input('Nacisnij dowolny klawisz by powrocic do menu ')
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '4':
            Zapis(planety)
            os.system('cls')  # czyszczenie działa na windowsowej konsoli
        elif wybor == '0':
            exit()


class Planety():
    nazwa = ''
    odleglosc_astro = 0
    czy_planeta = False


Start()



