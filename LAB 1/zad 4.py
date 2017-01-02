rok=int(input("Podaj rok do ananizy: "))
if rok%4!=0:
    print("Rok jest nieprzestępny.")
else:
    if rok%100!=0:
        print("Rok jest przestępny")
    elif rok%400!=0:
        print("Rok jest nieprzestępny")
    else:
        print("Rok jest przestepny")
