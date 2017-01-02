from math import pi

x=float(input("Podaj liczba x: "))
x2=x*x
a=pi**2
oblicz=(x2/a*(x2+0.5))*(1+x2/(a*(x2-0.5)))
print("oto wynik : ", oblicz)
