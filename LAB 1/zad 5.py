a=float(input("Podaj cene towaru: "))
netto=a/1.23
vat=a-netto
print("Cena netto: ", round(netto, 2))
print("Podatek VAT: ", round(vat, 2))
