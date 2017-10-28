# MonaLisaGenetic

### Czas: do końca października

### Czas

```python
    # Mutacja
    start_Mutacja = time.time()
    populacja = mutate(populacja, ilosc_w_populacji, wspolczynnik_mutacji, tab)
    print("Czas mutacji: %s" % (time.time() - start_Mutacja))
    # Ocena( 0 - 100 )
    start_Ocena = time.time()
    populacja = score(populacja, ilosc_w_populacji)
    print("Czas oceny: %s" % (time.time() - start_Ocena))
    # Zrzucanie najlepszego w populacji
    start_Zrzucanie = time.time()
    dump_best(populacja, p)
    print("Czas zrzucania: %s" % (time.time() - start_Zrzucanie))
    # Tworzenie poli rozrodczej do krzyżowania
    start_pole = time.time()
    pola_rozrodcza = matingpool(populacja, ilosc_w_populacji)
    print("Czas Pola: %s" % (time.time() - start_pole))
    # Krzyzowanie i nowa populacja
    start_cross = time.time()
    populacja = crossover(populacja, pola_rozrodcza)
    print("Czas Krossa: %s" % (time.time() - start_cross))
    print("---")




    Poszukać jakieś lepszej wersji mierzenia czy dwa obrazki są podobne
    Może coś lepszego algorytmicznie? Obadać jakieś rozwiązania
    Poszukać jakiś oszczędności czasowych
```