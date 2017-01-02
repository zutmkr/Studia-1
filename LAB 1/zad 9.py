potega=1
a=int(input("Podaj ile poteg policzyc: "))
if a==0:
    print("zła wartosc")
elif a<0:
    for n in range(-a):
        print("2 do potegi ", n, " to", potega)
        potega*=1/2
elif a>0:
    for n in range (a):
        print("2 do potegi ", n, "to ", potega)
