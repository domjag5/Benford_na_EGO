Program użyteczny do na ćwiczeniach z przedmiotu "E-gospodarka: narzędzia i bezpieczeństwo", prowadzonych w semsetrze letnim roku akademickiego 2021/2022 przez dr inż. Michała Rena na Wydziale Matematyki i Informatyki Uniwersytetu im Adama Mickiewicza w Poznaniu. Przygotowany do wykonywania zadania 1 z zajęć 7 i zadania 1 z zajęć 9 (https://renmich.faculty.wmi.amu.edu.pl/EGO/zajecia7.html i https://renmich.faculty.wmi.amu.edu.pl/EGO/zajecia9.html, dostęp: 17 maja 2022r.).

Działanie:
- znalezienie liter wszystkich dysków systemu Windows,
- przeszukanie wszystkich folderów na tych dyskach,
- stworzenie listy rozmiarów wszystkich plików (nie będących folderami) w bajtach,
- zebranie statystyk dotyczących rozmiaru i pierwszej cyfry rozmiarów,
- obliczenie średniej i odchylenia standardowego udziału procentowego rozmiarów kilku kategorii w losowo wybranym zestawie rozmiarów,
- porównanie statystyk dwudziestu dziewięciu zestawów rozmiarów podanych w treści zadania z wyliczonymi wcześniej statystykami i rozkładem Benforda,
- ocena każdego zestawu w skali od 0,00 (bardzo podobny)(wygląda jak wynik losowania plików z komputera) do 1,00 (niepodobny)(wygląda na oszustwo),
- przygotowanie pliku .csv z nazwami plików, ich oceną oraz liczbą porządkową.

Tekst mojej odpowiedzi do zadania 1 z zajęć 9:

Rozkład Benforda

Najsampierw wypada sprawdzić, czy pierwsze cyfry rozmiarów plików spełniają rozkład Benforda. Rozpatrzyłem oddzielnie pliki niepuste. Rozkład cyfr pośród nich jest podobny do rozkładu Benforda, choć oczywiście różni się w zależności od komputera. Dla pewności najlepiej byłoby przetestować wiele komputerów i uśrednić wyniki. Bazując na testach trzech maszyn, zdecydowałem się posłużyć tradycyjnym rozkładem Benforda, założywszy dodatkową tolerancję 2,0. Oznacza ona, że udział danej cyfry w zestawie może różnić się od udziału z rozkładu Benforda o dodatkowe 2 punkty procentowe, bez wzbudzania podejrzeń. Udział plików pustych w całkowitej liczbie plików ustaliłem na 1%, z dodatkową tolerancją 0,5. Rozkładów drugich i trzecich cyfr nie sprawdzałem, bo są zbyt podobne do równomiernego.

Dodatkowe kryterium

Dodatkowo postanowiłem rozpatrzyć długość rozmiaru w bajtach. Rozpiętość rozmiaru pliku jest duża, mało prawdopodobne, że wylosuje się zestaw z samymi plikami podobnej wielkości. Taki zestaw mógłby powstać przez przeszukanie części komputera lub wymyślanie rozmiarów przez osobę nie orientującą się w wielkościach plików. Sprawdziłem, ile na koputerze jest plików o rozmiarze jedno, dwu, trzy, cztero, pięciocyfrowym, oraz większych. Jako że te wielkości również różniły się w zależności od komputera, ustaliłem dodatkową tolerancję 0,4 dla rozmiarów jednocyfrowych i 2,0 dla pozostałych.

Ocena

Sprawdziłem, o ile udział rozmiarów danej kategorii może się różnić od średniej, nie wzbudzając podejrzeń. Wylosowałem 100 tysięcy zestawów po 100 rozmiarów i policzyłem odchylenie standardowe od średniej w każdej kategorii. Posłużyłem się estymatorem największej wiarygodności.
Początkowo każdemu zestawowi przyporzadkowywałem ocenę 0. Jeżeli w którejś kategorii wartość bezwzględna różnicy między udziałem w zestawie a średnią była większa niż suma odchylenia i tolerancji, dodawałam do oceny tę nadwyżkę. Na koniec zaokrąglałem ocenę do dwóch miejsc dziesiętnych i sprowadzałem do 1, jeśli była większa.

Program, który napisałem do pomocy, dostępny jest na stronie https://github.com/domjag5/Benford_na_EGO. Z pliku 006.txt usunąłem nadmiarowy rozmiar sto pierwszy.
