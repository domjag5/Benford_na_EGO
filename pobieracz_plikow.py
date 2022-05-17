import ctypes
import os
import pickle
import string


# funkcja znajdujaca litery wszystkich dyskow koputera z systemem windows
def znajdz_litery_dyskow():
    dyski = []
    # maska_bitowa - integer odpowiadajacy 26-cyfrowej liczbie binarnej,        00000010001000001000111100
    # porownujemy go z literami dyskow w kolejnosci alfabetycznej od prawej     ZYXWVUTSRQPONMLKJIHGFEDCBA
    # gdy nad litera jest 1, to na komputerze jest dysk o tej literze,          Dyski = [C, D, E, F, J, P, T]
    maska_bitowa = ctypes.windll.kernel32.GetLogicalDrives()
    # zmienna pomocnicza bo bedziemy degenerowac maske
    pom = maska_bitowa
    # string.ascii_uppercase - 26 liter od A do Z
    for litera in string.ascii_uppercase:
        # zaczynamy z prawej
        # bitowa operacja and (&) maski z int(1) da nam pierwsza cyfre z prawej (1 lub 0)
        # maska_bitowa = 10101    lub   1010
        #            1 = 00001          0001
        #              & -----        & ----
        #                00001 = 1      0000 = 0
        if (pom & 1) == 1:
            dyski.append(litera)
        # usuwamy pierwsza cyfre z prawej
        pom = pom >> 1
    return dyski


# Program znajduje wszystkie pliki na komputerze i sprawdza ich rozmiar w bajtach
# Nastepnie serializuje liste rozmiarow
def pobieracz_plikow():
    rozmiary_plikow = []
    for litera_dysku in znajdz_litery_dyskow():
        for root, subdirs, files in os.walk(str(litera_dysku) + ":\\"):
            for nazwa_pliku in files:
                sciezka_do_pliku = os.path.join(root, nazwa_pliku)
                if os.path.isfile(sciezka_do_pliku):
                    rozmiary_plikow.append(os.path.getsize(sciezka_do_pliku))
    pickle.dump(rozmiary_plikow, open("Obiekty\\rozmiary_plikow.pickle", "wb"))

# pobieracz_plikow()
