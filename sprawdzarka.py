import pickle

from zbieracz_statystyk import kategoria_dlugosci_rozmiaru

# tolerancje wynikające z różnych wyników na różnych komputerach
tolerancja_udzialu_kategorii_rozmiaru = [2.0 for _ in range(6)]
tolerancja_udzialu_kategorii_rozmiaru[0] = 0.4
tolerancja_udzialu_kategorii_pierwszej_cyfry = [2.0 for _ in range(10)]
tolerancja_udzialu_kategorii_pierwszej_cyfry[0] = 0.5


# Program ocenia pliki tekstowe od 001.txt do 029.txt
# Oceny zapisuje do pliku csv
def sprawdzarka():
    # pobranie wynikow funkcji zbieracz_statystyk()
    sredni_udzial_kategorii_rozmiaru = pickle.load(open("Obiekty\\sredni_udzial_kategorii_rozmiaru.pickle", "rb"))
    odchylenie_udzialu_kategorii_rozmiaru = pickle.load(
        open("Obiekty\\odchylenie_udzialu_kategorii_rozmiaru.pickle", "rb"))
    sredni_udzial_plikow_pustych = pickle.load(open("Obiekty\\sredni_udzial_plikow_pustych.pickle", "rb"))
    odchylenie_udzialu_plikow_pustych = pickle.load(open("Obiekty\\odchylenie_udzialu_plikow_pustych.pickle", "rb"))
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych = pickle.load(
        open("Obiekty\\sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych.pickle", "rb"))
    odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych = pickle.load(
        open("Obiekty\\odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych.pickle", "rb"))
    # slowniki porzadkujace dane do zapisu do pliku csv
    nazwa_na_ocene = {}
    nazwa_na_liczbe_porzadkowa = {}
    for numer_pliku in range(1001, 1030):
        # pobranie proby
        nazwa_pliku = str(numer_pliku)[1:] + ".txt"
        uwu = open("Benford\\" + nazwa_pliku)
        # readlines() nie wczytuje pustych linii z konca niektorych plikow
        proba = uwu.readlines()
        uwu.close()
        # sprawdzenie statystyk proby
        rozmiary = [0 for _ in range(6)]
        cyfry = [0 for _ in range(10)]
        for i in range(10):
            cyfry.append(0)
        for rozmiar in proba:
            rozmiary[kategoria_dlugosci_rozmiaru(int(rozmiar))] += 1
            pierwsza_cyfra = int(str(rozmiar)[0])
            cyfry[pierwsza_cyfra] += 1
        # porownanie odchylen od sredniej
        liczba_plikow_niepustych_w_probie = 100 - cyfry[0]
        ocena = 0
        for i in range(6):
            odchylenie_proby = abs(sredni_udzial_kategorii_rozmiaru[i] - rozmiary[i])
            normalne_odchylenie = odchylenie_udzialu_kategorii_rozmiaru[i] + tolerancja_udzialu_kategorii_rozmiaru[i]
            if odchylenie_proby > normalne_odchylenie:
                ocena += (odchylenie_proby - normalne_odchylenie)
        for i in range(10):
            if i == 0:
                odchylenie_proby = abs(sredni_udzial_plikow_pustych - cyfry[i])
                normalne_odchylenie = \
                    odchylenie_udzialu_plikow_pustych + tolerancja_udzialu_kategorii_pierwszej_cyfry[0]
            else:
                udzial_proby = (cyfry[i] / liczba_plikow_niepustych_w_probie) * 100
                odchylenie_proby = \
                    abs(sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i] - udzial_proby)
                normalne_odchylenie = \
                    odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i] + \
                    tolerancja_udzialu_kategorii_pierwszej_cyfry[i]
            if odchylenie_proby > normalne_odchylenie:
                ocena += (odchylenie_proby - normalne_odchylenie)
        nazwa_na_ocene[nazwa_pliku] = ocena
    # przypisanie plikom liczb od 1 dla najmniej do podejrzanego
    liczba_porzadkowa = 1
    for nazwa_pliku in dict(sorted(nazwa_na_ocene.items(), key=lambda pozycja: pozycja[1])):
        nazwa_na_liczbe_porzadkowa[nazwa_pliku] = liczba_porzadkowa
        liczba_porzadkowa += 1
    # zapisanie wynikow do pliku csv
    with open("464871.csv", "w", encoding="utf-8") as uwu:
        # w pierwszym wierszu etykiety kolumn
        uwu.write("nazwa,jak_bardzo_podejrzane,liczba porządkowa")
        for nazwa_pliku in nazwa_na_ocene:
            # sprowadzenie oceny do przedzialu <0;1> i dokladnosci 2 miejsc dziesietnych
            znormalizowana_ocena = nazwa_na_ocene[nazwa_pliku] / 100
            if znormalizowana_ocena > 1:
                znormalizowana_ocena = 1
            else:
                znormalizowana_ocena = round(znormalizowana_ocena, 2)
            liczba_porzadkowa = nazwa_na_liczbe_porzadkowa[nazwa_pliku]
            uwu.write("\n" + nazwa_pliku + "," + str(znormalizowana_ocena) + "," + str(liczba_porzadkowa))

# sprawdzarka()
