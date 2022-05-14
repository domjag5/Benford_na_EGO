import pickle


#
def sprawdzarka():
    srednia_ilosc_rozmiaru_danej_dlugosci = pickle.load(open("Obiekty\\srednie_ilosci_rozmiarow.pickle", "rb"))
    odchylenie_ilosci_rozmiaru_danej_dlugosci = pickle.load(open("Obiekty\\odchylenia_ilosci_rozmiarow.pickle", "rb"))
    srednia_ilosc_danej_pierwszej_cyfry = pickle.load(open("Obiekty\\srednie_ilosci_cyfr.pickle", "rb"))
    odchylenie_ilosci_danej_pierwszej_cyfry = pickle.load(open("Obiekty\\srednie_odchylenia_ilosci_cyfr.pickle", "rb"))
    #
    nazwa_na_ocene = {}
    nazwa_na_liczbe_porzadkowa = {}
    for numer_pliku in range(1001, 1030):
        ocena = 0
        nazwa_pliku = str(numer_pliku)[1:] + ".txt"
        uwu = open("Benford\\" + nazwa_pliku)
        proba = uwu.readlines()
        uwu.close()
        # tworzenie list wynikow proby
        rozmiary = []
        for i in range(6):
            rozmiary.append(0)
        cyfry = []
        for i in range(10):
            cyfry.append(0)
        for rozmiar in proba:
            rozmiar = int(rozmiar)
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
            odchylenie_proby = abs(srednia_ilosc_rozmiaru_danej_dlugosci[i] - rozmiary[i])
            if odchylenie_proby > odchylenie_ilosci_rozmiaru_danej_dlugosci[i]:
                ocena += (odchylenie_proby - odchylenie_ilosci_rozmiaru_danej_dlugosci[i])
        for i in range(10):
            odchylenie_proby = abs(srednia_ilosc_danej_pierwszej_cyfry[i] - cyfry[i])
            if odchylenie_proby > odchylenie_ilosci_danej_pierwszej_cyfry[i]:
                ocena += (odchylenie_proby - odchylenie_ilosci_danej_pierwszej_cyfry[i])

        nazwa_na_ocene[nazwa_pliku] = ocena / 100
    #
    liczba_porzadkowa = 1
    for nazwa_pliku in dict(sorted(nazwa_na_ocene.items(), key=lambda pozycja: pozycja[1])):
        nazwa_na_liczbe_porzadkowa[nazwa_pliku] = liczba_porzadkowa
        liczba_porzadkowa += 1
    #
    with open("464871.csv", "w", encoding="utf-8") as uwu:
        numer_linii_w_pliku = 1
        for nazwa_pliku in nazwa_na_ocene:
            liczba_porzadkowa = nazwa_na_liczbe_porzadkowa[nazwa_pliku]
            znormalizowana_ocena = nazwa_na_ocene[nazwa_pliku]
            if znormalizowana_ocena < 0:
                znormalizowana_ocena = 0
            elif znormalizowana_ocena > 1:
                znormalizowana_ocena = 1
            else:
                znormalizowana_ocena = round(znormalizowana_ocena, 2)
            if numer_linii_w_pliku == 1:
                uwu.write("nazwa,jak_bardzo_podejrzane,liczba porządkowa\n")
            if numer_linii_w_pliku == len(nazwa_na_ocene):
                uwu.write(nazwa_pliku + "," + str(znormalizowana_ocena) + "," + str(liczba_porzadkowa))
            else:
                uwu.write(nazwa_pliku + "," + str(znormalizowana_ocena) + "," + str(liczba_porzadkowa) + "\n")
            numer_linii_w_pliku += 1


sprawdzarka()
