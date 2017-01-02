a=float(input("Podaj zwoje zarobki: "))
if a<85528:
    print("Twój podatek wynosi: ", round(a*0.18-556.02, 0))
else:
    nadwyzka=a-85528
    print("Twoj podatk wynosi: ", round(14839.02+(nadwyzka*0.32),0))
