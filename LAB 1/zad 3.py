print("Witaj w klakulatorze")
print("Co chcesz zrobic?")
print("1-DODAC")
print("2-ODJAC")
print("3-WYMNOZYC")
print("4-PODZIELIC")
print("5-ZAKONCZYÆ PRACE")
x=int(input("Twoj wybor?: "))
a=float(input("Podaj liczbe a: "))
b=float(input("Podaj liczbe b: "))
if  x== 1:
    print("Wynik: ", a+b)
elif x == 2:
    print("Wynik: ", a-b)
elif x== 3:
    print("Wynik: ", a*b)
elif x == 4:
        if b!=0:
            print("Wynik: ", a/b)
        else:
            print("Nie mozna dzielic przez zero!")
else:
    print("Koniec Programu Klalkulator.")
