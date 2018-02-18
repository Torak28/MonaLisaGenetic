# MonaLisaGenetic

Aplikacja realizująca aproksymację obrazu przy pomocy algorytmu genetycznego.

Obraz zadany przez użytkownika na początku może być dowolny pod każdym względem. Końcowy obraz jest wynikiem losowego nakładania na siebie figur geometrycznych tak, by możliwie dobrze przypominał obraz źródłowy. Wszystkie parametry pracy programu, tj. współczynnik mutacji, wielkość populacji, czy ilość iteracji, są możliwe do modyfikacji według uznania użytkownika.

Aplikacja dzieli zadany obraz na zadaną przez użytkownika mniejszą ilość obrazów i przybliża je wykorzystując algorytm genetyczny. Pseudokod algorytmu wygląda następująco:

```
1. Losowanie populacji początkowej złożonej z X osobników
2. Jeśli nie koniec to:
	a. Mutacja
	b. Ocena wszystkich osobników
	c. Dopóki nowa populacja nie ma X chromosomów:
		A. Selekcja
		B. Krzyżowanie
		C. Dodanie do nowej populacji
	c. Zamiana starej populacji na nowa
```

### Wynik dzialania Programu w zależności od przyjętego trybu:

![alt](https://i.imgur.com/PMnPf3L.png)

Czas generacji: ok. 20 min

### Wersje:

 * **v1** - pierwsza wersja z kwadratami
 * **v2** - druga wersja z kołem, trójkątem i kwadratem
 * **v3** - trzecia wersja ze średnim kolorem i super szybkim liczeniem różnic
 * **v4** - czwarta wersja z podziełem na 4 części
 * **v5** - piąta wersja z podziałem na 16 i większą dozą automatyzacji tworzenia drzewa katalogów itd.
 * **v6** - szósta wersja z podziałem na 64 i brakiem okna
 * **v7** - siódma wersja z podziałem na 256 i nowym sposobem pisania od pliku. Sam podział poprawiony.
 * **v8** - ósma wersja z równoległym wykonaniem i naprawionymi kolorami.
 * **v9** - dziewiąta wersja z wykorzystaniem Cythona