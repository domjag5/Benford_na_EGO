import itertools
import os
import pickle
from glob import glob


# Program znajduje wszystkie pliki na dysku C i sprawdza ich rozmiar w bajtach
# Nastepnie serializuje liste rozmiarow
def pobieracz_plikow():
    # itertools.chain - sprawdza najpierw jedno, potem drugie
    # glob.glob - sprawdza wszystkie pliki w folderze
    # ** i recursive=True - wszystkie podfoldery
    # .** i recursive true - to co powyżej dla ukrytych plików
    sciezki_do_plikow = [f for f in itertools.chain(glob(r'C:\**', recursive=True), glob(r'C:\**\.*', recursive=True))
                         if
                         os.path.isfile(f)]
    wielkosci_plikow = []
    for f in sciezki_do_plikow:
        # czasem pliki znikaja podczas wykonywania programu albo nie mozna sie do nich dostac
        # jesli nie uda sie sprawdzenie rozmiaru pliku to uznajemy go za pusty
        # przy uzyciu innych narzedzi (komend) jest to prawdopodobny wynik
        rozmiar = 0
        try:
            rozmiar = os.path.getsize(rf'{f}')
        except OSError:
            pass
        wielkosci_plikow.append(rozmiar)
    # zapis do pliku pickle
    if not os.path.exists("Obiekty"):
        os.makedirs("Obiekty")
    pickle.dump(wielkosci_plikow, open("Obiekty\\rozmiary.pickle", "wb"))


pobieracz_plikow()
