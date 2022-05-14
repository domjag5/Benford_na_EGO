import pickle
#
srednia_ilosc_rozmiaru_danej_dlugosci=pickle.load(open("Obiekty\\srednie_ilosci_rozmiarow.pickle","rb"))
odchylenie_ilosci_rozmiaru_danej_dlugosci=pickle.load(open("Obiekty\\odchylenia_ilosci_rozmiarow.pickle","rb"))
srednia_ilosc_danej_pierwszej_cyfry=pickle.load(open("Obiekty\\srednie_ilosci_cyfr.pickle","rb"))
odchylenie_ilosci_danej_pierwszej_cyfry=pickle.load(open("Obiekty\\srednie_odchylenia_ilosci_cyfr.pickle","rb"))
for numer_pliku in range(1001,1030):
    wynik=0
    nazwa_pliku="Benford\\"+str(numer_pliku)[1:]+".txt"
    uwu=open(nazwa_pliku)
    proba=uwu.readlines()
    uwu.close()
    # tworzenie list wynikow proby
    rozmiary = []
    for i in range(6):
        rozmiary.append(0)
    cyfry = []
    for i in range(10):
        cyfry.append(0)
    for rozmiar in proba:
        rozmiar=int(rozmiar)
        if rozmiar < 10:
            rozmiary[0] += 1
        elif rozmiar < 100:
            rozmiary[1] += 1
        elif rozmiar < 1000:
            rozmiary[2] += 1
        elif rozmiar < 10000:
            rozmiary[3] += 1
        elif rozmiar < 100000:
            rozmiary[4] += 1
        else:
            rozmiary[5] += 1
        # ustalenie pierwszej cyfry rozmiaru pliku
        pierwsza_cyfra = int(str(rozmiar)[0])
        cyfry[pierwsza_cyfra] += 1
    # porownanie odchylenia od sredniej
    for i in range(6):
        odchylenie_proby=abs(srednia_ilosc_rozmiaru_danej_dlugosci[i]-rozmiary[i])
        if odchylenie_proby<=odchylenie_ilosci_rozmiaru_danej_dlugosci[i]:
            pass
        else:
            wynik+=(odchylenie_proby-odchylenie_ilosci_rozmiaru_danej_dlugosci[i])
    for i in range(10):
        odchylenie_proby=abs(srednia_ilosc_danej_pierwszej_cyfry[i]-cyfry[i])
        if odchylenie_proby<=odchylenie_ilosci_danej_pierwszej_cyfry[i]:
            pass
        else:
            wynik+=(odchylenie_proby-odchylenie_ilosci_danej_pierwszej_cyfry[i])
    if wynik<=0:
        wynik=0
    elif wynik>100:
        wynik=1
    else:
        wynik=round(wynik/100.0,2)
    print(wynik)