def DniWMiesiacu(miesiac, rok):
    lista31=[1,3,5,7,8,10,12]
    lista30=[4,6,9,11]
    if rok%4!=0:
        if miesiac in lista31:
            return 31
        elif miesiac==2:
            return 28
        elif miesiac in lista30:
            return 30
    else:
        if rok%100!=0:
            if miesiac in lista31:
                return 31
            elif miesiac==2:
                return 29
            elif miesiac in lista30:
                return 30
        elif rok%400!=0:
            if miesiac in lista31:
                return 31
            elif miesiac==2:
                return 28
            elif miesiac in lista30:
                return 30
        else:
            if miesiac in lista31:
                return 31
            elif miesiac==2:
                return 29
            elif miesiac in lista30:
                return 30

def DzienTygodnia(rok,miesiac=1,dzien=1):
    miesiac=miesiac-2
    if miesiac<=0:
        miesiac=miesiac+12
        rok=rok-1

    miesiac=miesiac*83//32
    t=(((((miesiac+dzien)+rok)+rok//4)-rok//100)+rok//400)
    t=t%7
    return t