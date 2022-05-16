import pickle

#
from zbieracz_statystyk import kategoria_dlugosci_rozmiaru

tolerancja_sredniej_ilosci_jednocyfrowych = 0.3
tolerancja_sredniej_ilosci_rozmiaru = 0.6
tolerancja_sredniej_ilosci_pierwszej_cyfry = 0.3


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
        # pobranie proby
        nazwa_pliku = str(numer_pliku)[1:] + ".txt"
        uwu = open("Benford\\" + nazwa_pliku)
        proba = uwu.readlines()
        uwu.close()
        # sprawdzenie statystyk proby
        rozmiary = []
        for i in range(6):
            rozmiary.append(0)
        cyfry = []
        for i in range(10):
            cyfry.append(0)
        for rozmiar in proba:
            rozmiary[kategoria_dlugosci_rozmiaru(int(rozmiar))]+=1
            pierwsza_cyfra = int(str(rozmiar)[0])
            cyfry[pierwsza_cyfra] += 1
        # porownanie odchylen od sredniej
        ocena = 0
        for i in range(0, 1):
            odchylenie_proby = abs(srednia_ilosc_rozmiaru_danej_dlugosci[i] - rozmiary[i])
            normalne_odchylenie = odchylenie_ilosci_rozmiaru_danej_dlugosci[
                                      i] + tolerancja_sredniej_ilosci_jednocyfrowych
            if odchylenie_proby > normalne_odchylenie:
                ocena += (odchylenie_proby - normalne_odchylenie)
        for i in range(1, 6):
            odchylenie_proby = abs(srednia_ilosc_rozmiaru_danej_dlugosci[i] - rozmiary[i])
            normalne_odchylenie = odchylenie_ilosci_rozmiaru_danej_dlugosci[i] + tolerancja_sredniej_ilosci_rozmiaru
            if odchylenie_proby > normalne_odchylenie:
                ocena += (odchylenie_proby - normalne_odchylenie)
        for i in range(10):
            odchylenie_proby = abs(srednia_ilosc_danej_pierwszej_cyfry[i] - cyfry[i])
            normalne_odchylenie = odchylenie_ilosci_danej_pierwszej_cyfry[
                                      i] + tolerancja_sredniej_ilosci_pierwszej_cyfry
            if odchylenie_proby > normalne_odchylenie:
                ocena += (odchylenie_proby - normalne_odchylenie)

        nazwa_na_ocene[nazwa_pliku] = ocena / 100
    ##
    liczba_porzadkowa = 1
    for nazwa_pliku in dict(sorted(nazwa_na_ocene.items(), key=lambda pozycja: pozycja[1])):
        nazwa_na_liczbe_porzadkowa[nazwa_pliku] = liczba_porzadkowa
        liczba_porzadkowa += 1
    #
    with open("464871.csv", "w", encoding="utf-8") as uwu:
        # w pierwszym wierszu etykiety kolumn
        uwu.write("nazwa,jak_bardzo_podejrzane,liczba porządkowa")
        for nazwa_pliku in nazwa_na_ocene:
            # sprowadzenie oceny do przedzialu <0;1> i dokladnosci 2 miejsc dziesietnych
            znormalizowana_ocena = nazwa_na_ocene[nazwa_pliku]
            if znormalizowana_ocena > 1:
                znormalizowana_ocena = 1
            else:
                znormalizowana_ocena = round(znormalizowana_ocena, 2)
            liczba_porzadkowa = nazwa_na_liczbe_porzadkowa[nazwa_pliku]
            uwu.write("\n"+nazwa_pliku + "," + str(znormalizowana_ocena) + "," + str(liczba_porzadkowa))


sprawdzarka()
