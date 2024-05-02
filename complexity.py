import numpy as np
from itertools import product
import time
import random
import matplotlib.pyplot as plt


# zadanie 1
# Dla listy liczb zadanej przez użytkownika, zaimplementuj algorytm (algorytmy)
# 1. znajdujący największy element na liście,
# 2. znajdujący drugi największy element na liście,
# 3. obliczający średnią elementów na liście

def zadanie1(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    print(f'Największy element to {lista[0]}')
    if len(lista) > 1:
        print(f'Drugi największy element to {lista[1]}')

    suma = 0
    for i in lista:
        suma = suma + int(i)
    print(f'Średnia elementów to {suma / len(lista)}')
    print(f'Lista: {lista}')

# lista = list(input('Podaj ciąg liczb: '))
# zadanie1(lista)


# zadanie 2
# Zaimplementuj algorytm mnożący dwie macierze kwadratowe zadane przez użytkownika.

def wczytaj_macierz():
    m = int(input("Podaj liczbę wierszy macierzy: "))
    n = int(input("Podaj liczbę kolumn macierzy: "))
    macierz = []
    print("Podaj elementy macierzy po jednym w wierszu:")
    for i in range(m):
        wiersz = []
        for j in range(n):
            wiersz.append(float(input()))
        macierz.append(wiersz)
    return macierz


def mnozenie_macierzy(macierz1, macierz2):
    n = len(macierz1)
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += macierz1[i][k] * macierz2[k][j]
    print(np.array(result))


# macierz1 = np.array(wczytaj_macierz())
# macierz2 = np.array(wczytaj_macierz())
# mnozenie_macierzy(macierz1, macierz2)

# zadanie 3
# Dany jest zbiór liczb całkowitych A zadanych przez użytkownika. Zweryfikuj (testując wszystkie możliwe
# kombinacje) czy dla jakiegokolwiek podzbioru zbioru A suma liczb jest równa dokładnie 0.


def zadanie3(A):
    d = len(A)
    decisions = list(product([0, 1], repeat=d))

    exist = False
    for decision in decisions:
        dec = list(decision)
        suma = np.dot(A, dec)
        if suma == 0 and np.sum(dec) != 0:
            exist = True
            idx = []
            for i in range(len(dec)):
                if dec[i] == 1:
                    idx.append(i)
            print([A[id] for id in idx])

    if not exist:
        print('Nie ma takich podzbiorów.')
    else:
        print(f'Mamy takie podzbiory dla listy: {A}')


#d = int(input('Podaj wielkość zbioru: '))
#A = []
#for i in range(d):
#    A.append(int(input('Podaj liczbę: ')))
#zadanie3(A)


# zadanie 4
def zmierz_czas(func, *args, **kwargs):
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


def zadanie4_1(n):
    lista = [random.randint(0, 9) for _ in range(n)]
    return zmierz_czas(zadanie1, lista)


#n1 = int(input('Długość listy: '))
#print(zadanie4_1(n1))

def zadanie4_2(n):
    m1 = np.random.randint(0, 10, size=(n, n))
    m2 = np.random.randint(0, 10, size=(n, n))
    return zmierz_czas(mnozenie_macierzy, m1, m2)


#n2 = int(input('Wielkość macierzy: '))
#print(zadanie4_2(n2))

def zadanie4_3(n):
    lista = [random.randint(-10, 10) for _ in range(n)]
    return zmierz_czas(zadanie3, lista)


#n3 = int(input('Długość listy: '))
#print(zadanie4_3(n3))

# zadanie 5

lista_srednich_1 = []
lista_min_1 = []
lista_max_1 = []

lista_srednich_2 = []
lista_min_2 = []
lista_max_2 = []

lista_srednich_3 = []
lista_min_3 = []
lista_max_3 = []


def zadanie5(lista_srednich, lista_min, lista_max, func):
    for i in range(1, 11):
        n = i
        lista_dla_n = []
        for j in range(11):
            if func(n) > 10:
                return f'Przerwano działanie, ponieważ czas przekroczył 10 min.'
            else:
                lista_dla_n.append(func(n))
        lista_srednich.append(np.mean(lista_dla_n))
        lista_min.append(min(lista_dla_n))
        lista_max.append(max(lista_dla_n))


def wykresy(lista_srednich, lista_min, lista_max, func):

    zadanie5(lista_srednich, lista_min, lista_max, func)

    fig, axs = plt.subplots(3)

    axs[0].plot(range(10), lista_srednich,  color='blue')
    axs[0].set_title('Wykres 1 - Średnie')

    # Wykres 2
    axs[1].plot(range(10), lista_min, color='red')
    axs[1].set_title('Wykres 2 - Min')

    # Wykres 3
    axs[2].plot(range(10), lista_max, color='green')
    axs[2].set_title('Wykres 3 - Max')

    # Ustawienie odstępów między podwykresami
    plt.tight_layout()

    # Wyświetlenie wykresu
    plt.show()

wykresy(lista_srednich_1, lista_min_1, lista_max_1, zadanie4_1)
