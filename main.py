def tabliczka_ramka(rozmiar):
    for i in range(1,rozmiar+1):
        for j in range (1,rozmiar+1):
            if i==1 or j==1 or i==rozmiar or j==rozmiar:
                print("*")
            else:
                print(" ")
        print()





def tabliczka_mnozenia(rozmiar):
    for i in range(1, rozmiar + 1):
        for j in range(1, rozmiar + 1):
            wynik = i + j
            print(f'{i} * {j} = {wynik}', end='\t')
        print()
def tabliczka_gwiazdki(rozmiar):
    for i in range(1,rozmiar+1):
        for j in range(1,rozmiar+1):
            print("*")
        print()

rozmiar_tabliczki: int = 5
tabliczka_mnozenia(rozmiar_tabliczki)

tabliczka_ramka(rozmiar_tabliczki)

tabliczka_gwiazdki(rozmiar_tabliczki)

