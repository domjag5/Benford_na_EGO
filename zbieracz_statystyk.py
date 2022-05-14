import random
from statistics import mean
from math import sqrt
import pickle
#
# funkcja obliczajaca odchylenie standardowe
def estymator_najwiekszej_wiarygodnosci(lista):
    srednia=mean(lista)
    suma=0
    for i in lista:
        suma+=pow((float(i)-srednia),2)
    return sqrt(suma/len(lista))
#
rozmiary_plikow=pickle.load(open("Obiekty\\rozmiary.pickle", "rb"))
# STATYSTYKI PRZESZUKANIA CALEGO KOMPUTERA
# tworzenie list wynikow przeszukania calego komputera
rozmiary = []
for i in range(6):
    rozmiary.append(0)
cyfry = []
for i in range(10):
    cyfry.append(0)
for rozmiar in rozmiary_plikow:
    # ustalenie ilosci cyfr rozmiaru pliku
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
# zapis statystyk przeszukania calego komputera do pilku
uwu=open("statystyki.txt",'w')
razem_plikow = len(rozmiary_plikow)
uwu.write("Na komputerze: \n")
uwu.write("razem plikow " + str(razem_plikow) + "\n")
uwu.write("jednocyfrowych ( < 10 B )                       " + str(round((float(rozmiary[0]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("dwucyfrowych ( < 100 B )                        " + str(round((float(rozmiary[1]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("trzycyfrowych ( < 1000 B )                      " + str(round((float(rozmiary[2]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("czterocyfrowych ( < 10000 B )                   " + str(round((float(rozmiary[3]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("pieciocyfrowych ( < 100 000 B )                 " + str(round((float(rozmiary[4]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("szesciocyfrowych i wiekszych ( >= 100 000 B )   " + str(round((float(rozmiary[5]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("Zaczynajacych sie na: \n")
for i in range(10):
    uwu.write(str(i) + ": " + str(round((float(cyfry[i]) / razem_plikow) * 100, 1)) + "%\n")
uwu.write("\n")
# STATYSTYKI 100000 LOSOWAN 100 LICZB
# tworzenie list wynikow wszystkich prob
ilosci_rozmiaru_danej_dlugosci = []
for i in range(6):
    ilosci_rozmiaru_danej_dlugosci.append([])
ilosci_danej_pierwszej_cyfry =[]
for i in range(10):
    ilosci_danej_pierwszej_cyfry.append([])
# przeprowadzanie prob
for p in range(100000):
    # tworzenie list wynikow proby
    rozmiary = []
    for i in range(6):
        rozmiary.append(0)
    cyfry = []
    for i in range(10):
        cyfry.append(0)
    # nowy losowy zbior
    random.random()
    for rozmiar in random.sample(rozmiary_plikow, 100):
        # ustalenie ilosci cyfr rozmiaru pliku
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
    # dodanie wyniku proby do list wszystkich wynikow
    for k in range(6):
        ilosci_rozmiaru_danej_dlugosci[k].append(rozmiary[k])
    for k in range(10):
        ilosci_danej_pierwszej_cyfry[k].append(cyfry[k])
    # # zapis statystyk proby do pilku
    # uwu.write("probka nr " + str(int(p+1)) + "\n")
    # for i in range(6):
    #     uwu.write(str(i+1)+"-cyfr:            " + str(rozmiary[i]) + "\n")
    # for i in range(10):
    #     uwu.write("["+str(i)+"]: "+ str(cyfry[i]) + "\n")
    # uwu.write("\n")
# obliczenie srednich i odchylen standardowych i zapis do pliku statystyk
srednia_ilosc_rozmiaru_danej_dlugosci=[]
odchylenie_ilosci_rozmiaru_danej_dlugosci=[]
srednia_ilosc_danej_pierwszej_cyfry=[]
odchylenie_ilosci_danej_pierwszej_cyfry=[]
for i in range(6):
    srednia_ilosc_rozmiaru_danej_dlugosci.append(mean(ilosci_rozmiaru_danej_dlugosci[i]))
    odchylenie_ilosci_rozmiaru_danej_dlugosci.append(estymator_najwiekszej_wiarygodnosci(ilosci_rozmiaru_danej_dlugosci[i]))
    uwu.write(str(i+1) +"-cyfr: " + str(round(srednia_ilosc_rozmiaru_danej_dlugosci[i], 1)) + "  ")
    uwu.write("odchylenie: " + str(round(odchylenie_ilosci_rozmiaru_danej_dlugosci[i], 1)) + "\n")
for i in range(10):
    srednia_ilosc_danej_pierwszej_cyfry.append(mean(ilosci_danej_pierwszej_cyfry[i]))
    odchylenie_ilosci_danej_pierwszej_cyfry.append(estymator_najwiekszej_wiarygodnosci(ilosci_danej_pierwszej_cyfry[i]))
    uwu.write("["+str(i)+"] "+str(round(srednia_ilosc_danej_pierwszej_cyfry[i], 1)) + "  ")
    uwu.write("odchylenie: "+str(round(odchylenie_ilosci_danej_pierwszej_cyfry[i], 1)) + "\n")
uwu.close()
# zapis do plikow pickle
pickle.dump(srednia_ilosc_rozmiaru_danej_dlugosci,open("Obiekty\\srednie_ilosci_rozmiarow.pickle","wb"))
pickle.dump(odchylenie_ilosci_rozmiaru_danej_dlugosci,open("Obiekty\\odchylenia_ilosci_rozmiarow.pickle","wb"))
pickle.dump(srednia_ilosc_danej_pierwszej_cyfry,open("Obiekty\\srednie_ilosci_cyfr.pickle","wb"))
pickle.dump(odchylenie_ilosci_danej_pierwszej_cyfry,open("Obiekty\\srednie_odchylenia_ilosci_cyfr.pickle","wb"))