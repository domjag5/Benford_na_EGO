import pickle
import random
from math import sqrt
from statistics import mean


# Program analizuje liste rozmiarow plikow
# oraz 100'000 probek 100 rozmiarow, wybieranych losowo
# Zlicza liczbe rozmiarow w 6 kategoriach dlugosci w bajtach
# oraz liczbe rozmiarow zaczynajacych sie kazda cyfra
# Oblicza srednia i odchylenie standardowe powyzszych wielkosci w losowych probach
# Zapisuje podsumowanie statystyk do pliku tekstowego
# Serializuje listy srednich i odchylen
#
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


def zapisz_statystyki_calego_komputera_do_pliku(pisacz_do_pliku, rozmiary, cyfry, razem_plikow):
    plikow_niepustych=razem_plikow-cyfry[0]
    pisacz_do_pliku.write("Na komputerze: \n")
    pisacz_do_pliku.write("razem plikow " + str(razem_plikow) + "\n")
    pisacz_do_pliku.write("jednocyfrowych ( < 10 B )                       " + str(
        round((float(rozmiary[0]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("dwucyfrowych ( < 100 B )                        " + str(
        round((float(rozmiary[1]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("trzycyfrowych ( < 1000 B )                      " + str(
        round((float(rozmiary[2]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("czterocyfrowych ( < 10000 B )                   " + str(
        round((float(rozmiary[3]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("pieciocyfrowych ( < 100 000 B )                 " + str(
        round((float(rozmiary[4]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("szesciocyfrowych i wiekszych ( >= 100 000 B )   " + str(
        round((float(rozmiary[5]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("Zaczynajacych sie na: \n")
    for i in range(10):
        pisacz_do_pliku.write(str(i) + ": " + str(round((float(cyfry[i]) / razem_plikow) * 100, 1)) + "%\n")
    pisacz_do_pliku.write("\n")

def zbieracz_statystyk():
    # lista rozmiarow - wynik funkcji pobieracz_plikow()
    rozmiary_plikow = pickle.load(open("Obiekty\\rozmiary.pickle", "rb"))
    # STATYSTYKI PRZESZUKANIA CALEGO KOMPUTERA
    rozmiary = []
    for i in range(6):
        rozmiary.append(0)
    cyfry = []
    for i in range(10):
        cyfry.append(0)
    for rozmiar in rozmiary_plikow:
        rozmiary[kategoria_dlugosci_rozmiaru(rozmiar)]+=1
        pierwsza_cyfra = int(str(rozmiar)[0])
        cyfry[pierwsza_cyfra] += 1
    uwu=open("statystyki.txt","w")
    zapisz_statystyki_calego_komputera_do_pliku(uwu,rozmiary,cyfry,len(rozmiary_plikow))
    # STATYSTYKI 100'000 LOSOWAN 100 LICZB
    # listy wynikow wszystkich prob
    ilosci_rozmiaru_danej_dlugosci = []
    for i in range(6):
        ilosci_rozmiaru_danej_dlugosci.append([])
    ilosci_danej_pierwszej_cyfry = []
    for i in range(10):
        ilosci_danej_pierwszej_cyfry.append([])
    for proba in range(100000):
        rozmiary = []
        for i in range(6):
            rozmiary.append(0)
        cyfry = []
        for i in range(10):
            cyfry.append(0)
        # nowy losowy zbior
        random.random()
        for rozmiar in random.sample(rozmiary_plikow, 100):
            rozmiary[kategoria_dlugosci_rozmiaru(rozmiar)]+=1
            pierwsza_cyfra = int(str(rozmiar)[0])
            cyfry[pierwsza_cyfra] += 1
        # dodanie wyniku proby do list wszystkich wynikow
        for k in range(6):
            ilosci_rozmiaru_danej_dlugosci[k].append(rozmiary[k])
        for k in range(10):
            ilosci_danej_pierwszej_cyfry[k].append(cyfry[k])
        # # zapis statystyk proby do pilku
        # uwu.write("probka nr " + str(int(proba+1)) + "\n")
        # for i in range(6):
        #     uwu.write(str(i+1)+"-cyfr:            " + str(rozmiary[i]) + "\n")
        # for i in range(10):
        #     uwu.write("["+str(i)+"]: "+ str(cyfry[i]) + "\n")
        # uwu.write("\n")
    # obliczenie srednich i odchylen standardowych i zapis do pliku statystyk
    srednia_ilosc_rozmiaru_danej_dlugosci = []
    odchylenie_ilosci_rozmiaru_danej_dlugosci = []
    srednia_ilosc_danej_pierwszej_cyfry = []
    odchylenie_ilosci_danej_pierwszej_cyfry = []
    for i in range(6):
        srednia_ilosc_rozmiaru_danej_dlugosci.append(mean(ilosci_rozmiaru_danej_dlugosci[i]))
        odchylenie_ilosci_rozmiaru_danej_dlugosci.append(
            estymator_najwiekszej_wiarygodnosci(ilosci_rozmiaru_danej_dlugosci[i]))
        uwu.write(str(i + 1) + "-cyfr: " + str(round(srednia_ilosc_rozmiaru_danej_dlugosci[i], 1)) + "  ")
        uwu.write("odchylenie: " + str(round(odchylenie_ilosci_rozmiaru_danej_dlugosci[i], 1)) + "\n")
    for i in range(10):
        srednia_ilosc_danej_pierwszej_cyfry.append(mean(ilosci_danej_pierwszej_cyfry[i]))
        odchylenie_ilosci_danej_pierwszej_cyfry.append(
            estymator_najwiekszej_wiarygodnosci(ilosci_danej_pierwszej_cyfry[i]))
        uwu.write("[" + str(i) + "] " + str(round(srednia_ilosc_danej_pierwszej_cyfry[i], 1)) + "  ")
        uwu.write("odchylenie: " + str(round(odchylenie_ilosci_danej_pierwszej_cyfry[i], 1)) + "\n")
    uwu.close()
    # dla cyfr jednak czysty benford
    srednia_ilosc_danej_pierwszej_cyfry[1]=31.1
    # zapis list srednich i odchylen do plikow pickle
    pickle.dump(srednia_ilosc_rozmiaru_danej_dlugosci, open("Obiekty\\srednie_ilosci_rozmiarow.pickle", "wb"))
    pickle.dump(odchylenie_ilosci_rozmiaru_danej_dlugosci, open("Obiekty\\odchylenia_ilosci_rozmiarow.pickle", "wb"))
    pickle.dump(srednia_ilosc_danej_pierwszej_cyfry, open("Obiekty\\srednie_ilosci_cyfr.pickle", "wb"))
    pickle.dump(odchylenie_ilosci_danej_pierwszej_cyfry, open("Obiekty\\srednie_odchylenia_ilosci_cyfr.pickle", "wb"))


zbieracz_statystyk()
