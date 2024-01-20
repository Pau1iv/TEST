def tabliczka_mnozenia(rozmiar):
    for i in range(1, rozmiar + 1):
        for j in range(1, rozmiar + 1):
            wynik = i * j
            print(f'{i} * {j} = {wynik}', end='\t')
        print()


rozmiar_tabliczki: int = 10
tabliczka_mnozenia(rozmiar_tabliczki)
