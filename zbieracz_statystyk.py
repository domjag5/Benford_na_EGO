import pickle
import random
from math import sqrt
from statistics import mean


# FUNKCJE
# funkcja obliczajaca odchylenie standardowe
def estymator_najwiekszej_wiarygodnosci(lista_wartosci):
    srednia = mean(lista_wartosci)
    suma = 0
    for x in lista_wartosci:
        suma += pow((float(x) - srednia), 2)
    return sqrt(suma / len(lista_wartosci))


# ustalenie liczby cyfr rozmiaru pliku
def kategoria_dlugosci_rozmiaru(rozmiar):
    if rozmiar < 10:
        return 0
    elif rozmiar < 100:
        return 1
    elif rozmiar < 1000:
        return 2
    elif rozmiar < 10000:
        return 3
    elif rozmiar < 100000:
        return 4
    else:
        return 5


def zapisz_statystyki_calego_komputera_do_pliku(pisacz_do_pliku, rozmiary, cyfry, liczba_wszystkich_plikow):
    liczba_plikow_pustych = cyfry[0]
    liczba_plikow_niepustych = liczba_wszystkich_plikow - liczba_plikow_pustych
    pisacz_do_pliku.write("Na komputerze: \n")
    pisacz_do_pliku.write("razem plików " + str(liczba_wszystkich_plikow) + "\n")
    pisacz_do_pliku.write("jednocyfrowych ( < 10 B )                       " + str(
        round((float(rozmiary[0]) / liczba_wszystkich_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("dwucyfrowych ( < 100 B )                        " + str(
        round((float(rozmiary[1]) / liczba_wszystkich_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("trzycyfrowych ( < 1000 B )                      " + str(
        round((float(rozmiary[2]) / liczba_wszystkich_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("czterocyfrowych ( < 10000 B )                   " + str(
        round((float(rozmiary[3]) / liczba_wszystkich_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("pięciocyfrowych ( < 100 000 B )                 " + str(
        round((float(rozmiary[4]) / liczba_wszystkich_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("sześciocyfrowych i wiekszych ( >= 100 000 B )   " + str(
        round((float(rozmiary[5]) / liczba_wszystkich_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write(
        "pustych " + str(round((float(liczba_plikow_pustych) / liczba_wszystkich_plikow) * 100, 1)) + "\n")
    pisacz_do_pliku.write("Pośród plikow niepustych: \n")
    pisacz_do_pliku.write("Zaczynających sie na: \n")
    for i in range(1, 10):
        pisacz_do_pliku.write(str(i) + ": " + str(round((float(cyfry[i]) / liczba_plikow_niepustych) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("\n")


# Program analizuje liste rozmiarow plikow
# oraz 100'000 probek 100 rozmiarow, wybieranych losowo
# Zlicza liczbe rozmiarow w 6 kategoriach dlugosci w bajtach
# oraz liczbe rozmiarow zaczynajacych sie kazda cyfra
# Oblicza srednia i odchylenie standardowe powyzszych wielkosci w losowych probach
# Zapisuje podsumowanie statystyk do pliku tekstowego
# Serializuje listy srednich i odchylen
def zbieracz_statystyk():
    # lista rozmiarow i liczba plikow pustych - wynik funkcji pobieracz_plikow()
    rozmiary_plikow = pickle.load(open("Obiekty\\rozmiary_plikow.pickle", "rb"))
    # STATYSTYKI PRZESZUKANIA CALEGO KOMPUTERA
    rozmiary = [0 for _ in range(6)]
    cyfry = [0 for _ in range(10)]
    for rozmiar in rozmiary_plikow:
        rozmiary[kategoria_dlugosci_rozmiaru(rozmiar)] += 1
        pierwsza_cyfra = int(str(rozmiar)[0])
        cyfry[pierwsza_cyfra] += 1
    uwu = open("statystyki.txt", "w", encoding="utf-8")
    zapisz_statystyki_calego_komputera_do_pliku(uwu, rozmiary, cyfry, len(rozmiary_plikow))
    # STATYSTYKI 100'000 LOSOWAN 100 LICZB
    # listy wynikow wszystkich prob
    liczebnosci_kategorii_dlugosci = [[] for _ in range(6)]
    liczebnosci_kategorii_pierwszej_cyfry = [[] for _ in range(10)]
    udzialy_kategorii_pierwszej_cyfry_posrod_plikow_niepustych = [[] for _ in range(10)]
    for proba in range(100000):
        rozmiary = [0 for _ in range(6)]
        cyfry = [0 for _ in range(10)]
        for rozmiar in random.sample(rozmiary_plikow, 100):
            rozmiary[kategoria_dlugosci_rozmiaru(rozmiar)] += 1
            pierwsza_cyfra = int(str(rozmiar)[0])
            cyfry[pierwsza_cyfra] += 1
        # dodanie wyniku proby do list wszystkich wynikow
        for k in range(6):
            liczebnosci_kategorii_dlugosci[k].append(rozmiary[k])
        for k in range(10):
            liczebnosci_kategorii_pierwszej_cyfry[k].append(cyfry[k])
        liczba_plikow_niepustych_w_probie = 100 - cyfry[0]
        for k in range(1, 10):
            udzialy_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[k].append(
                (cyfry[k] / liczba_plikow_niepustych_w_probie) * 100)
        # # zapis statystyk proby do pilku
        # uwu.write("probka nr " + str(int(proba+1)) + "\n")
        # for i in range(6):
        #     uwu.write(str(i+1)+"-cyfr:            " + str(rozmiary[i]) + "\n")
        # for i in range(10):
        #     uwu.write("["+str(i)+"]: "+ str(cyfry[i]) + "\n")
        # uwu.write("\n")
    # obliczenie srednich i odchylen standardowych i zapis do pliku statystyk
    sredni_udzial_kategorii_rozmiaru = [0.0 for _ in range(6)]
    odchylenie_udzialu_kategorii_rozmiaru = [0.0 for _ in range(6)]
    sredni_udzial_plikow_pustych = None
    odchylenie_udzialu_plikow_pustych = None
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych = [0.0 for _ in range(10)]
    odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych = [0.0 for _ in range(10)]
    for i in range(6):
        sredni_udzial_kategorii_rozmiaru[i] = mean(liczebnosci_kategorii_dlugosci[i])
        odchylenie_udzialu_kategorii_rozmiaru[i] = estymator_najwiekszej_wiarygodnosci(
            liczebnosci_kategorii_dlugosci[i])
        uwu.write(str(i + 1) + "-cyfr: " + str(round(sredni_udzial_kategorii_rozmiaru[i], 1)) + " %  ")
        uwu.write("odchylenie: " + str(round(odchylenie_udzialu_kategorii_rozmiaru[i], 1)) + "\n")
    # dla zera
    for i in range(0, 1):
        sredni_udzial_plikow_pustych = mean(liczebnosci_kategorii_pierwszej_cyfry[0])
        odchylenie_udzialu_plikow_pustych = estymator_najwiekszej_wiarygodnosci(
            liczebnosci_kategorii_pierwszej_cyfry[0])
        uwu.write("[pustych] " + str(round(sredni_udzial_plikow_pustych, 1)) + " %  ")
        uwu.write("odchylenie: " + str(round(odchylenie_udzialu_plikow_pustych, 1)) + "\n")
    uwu.write("Pośród plikow niepustych:\n")
    for i in range(1, 10):
        sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i] = mean(
            udzialy_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i])
        odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i] = estymator_najwiekszej_wiarygodnosci(
            udzialy_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i])
        uwu.write("[" + str(i) + "] " + str(
            round(sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i], 1)) + " %  ")
        uwu.write("odchylenie: " + str(
            round(odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[i], 1)) + "\n")
    uwu.close()
    # dla zera usrednione 1
    sredni_udzial_plikow_pustych = 1
    # dla cyfr 1-9 jednak czysty benford
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[1] = 30.1
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[2] = 17.6
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[3] = 12.5
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[4] = 9.7
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[5] = 7.9
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[6] = 6.7
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[7] = 5.8
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[8] = 5.1
    sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych[9] = 4.6
    # zapis list srednich i odchylen do plikow pickle
    pickle.dump(sredni_udzial_kategorii_rozmiaru, open("Obiekty\\sredni_udzial_kategorii_rozmiaru.pickle", "wb"))
    pickle.dump(odchylenie_udzialu_kategorii_rozmiaru,
                open("Obiekty\\odchylenie_udzialu_kategorii_rozmiaru.pickle", "wb"))
    pickle.dump(sredni_udzial_plikow_pustych, open("Obiekty\\sredni_udzial_plikow_pustych.pickle", "wb"))
    pickle.dump(odchylenie_udzialu_plikow_pustych, open("Obiekty\\odchylenie_udzialu_plikow_pustych.pickle", "wb"))
    pickle.dump(sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych,
                open("Obiekty\\sredni_udzial_kategorii_pierwszej_cyfry_posrod_plikow_niepustych.pickle", "wb"))
    pickle.dump(odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych,
                open("Obiekty\\odchylenie_udzialu_kategorii_pierwszej_cyfry_posrod_plikow_niepustych.pickle", "wb"))

# zbieracz_statystyk()
