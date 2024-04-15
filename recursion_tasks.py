import numpy as np
import time
import matplotlib.pyplot as plt
import networkx as nx


# zadanie 1
def ciag1(n):
    if n <= 0:
        return 1
    return 3 ** n + ciag1(n - 1)


def ciag2(n):
    if n <= 0:
        return 0
    return n + ciag2(n - 2)


def ciag3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return ciag3(n - 1) + ciag3(n - 2)


def anal1(n):
    sum = 0
    for i in range(n + 1):
        sum += 3 ** i
    return sum

def anal11(n):
    return (3 ** (n + 1) - 1) // 2


def anal2(n):
    sum = 0
    if n % 2 == 0:
        for i in range(int(n / 2) + 1):
            sum += 2 * i
    else:
        for j in range(int((n + 1) / 2)):
            sum += 2 * j + 1
    return sum

def anal22(n):
    if n % 2 == 0:  # n is even
        return int((n / 2 + 1) * (n / 2))
    else:  # n is odd
        return int((n+3)/2 * (n+1)/2)

def anal3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        p = [1, 1]
        for i in range(2, n):  # zaczynam od 2 bo już pierwsze 2 jedynki przechowuje na liscie
            sum = p[i - 1] + p[i - 2]
            p.append(sum)
        return p[-1]

def anal33(n):
    sqrt_5 = np.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi ** n - psi ** n) / sqrt_5)


def check(func1, func2):
    l = list(input('Podaj ciąg liczb: '))
    for n in l:
        n = int(n)
        print(f'Wartość n: {n}')
        print(f'Wartość wyliczana rekurencyjnie wynosi: {func1(n)}, a wartość wyliczana analitycznie: {func2(n)}\n')

print('zadanie 1')
check(ciag3, anal33)

# zad 2 zgodne z poleceniem xd

def max_num(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        srodek = len(lista) // 2
        max_lewej = max_num(lista[:srodek])
        max_prawej = max_num(lista[srodek:])
        return max(max_lewej, max_prawej)

def second_max_num(lista):
    if len(lista) == 1:
      return lista[0]
    elif len(lista) == 2:
        return lista[0] if lista[0] < lista[1] else lista[1]
    else:
        max_element = max_num(lista)
        lista = [x for x in lista if x != max_element]
        return max_num(lista)

def max_element2(lista, actual_max, second_max):  # w tej od razu daje 2 te maxy więc chyba lepiej
    if len(lista) == 0:
        return actual_max, second_max
    elif len(lista) == 1:
        if lista[0] >= actual_max:
            return lista[0], actual_max
        elif lista[0] > second_max:
            return actual_max, lista[0]
        else:
            return actual_max, second_max
    else:
        half = len(lista) // 2
        left_actual_max, left_second_max = max_element2(lista[:half], actual_max, second_max)
        right_actual_max, right_second_max = max_element2(lista[half:], actual_max, second_max)

        actual_max = max(left_actual_max, right_actual_max)

        if left_actual_max > right_actual_max:
            second_max = max(left_second_max, right_actual_max)
        else:
            second_max = max(right_second_max, left_actual_max)

        return actual_max, second_max


def mean2(lista):
    lista = [int(x) for x in lista]
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        half = len(lista) // 2
        left = mean2(lista[:half])
        right = mean2(lista[half:])
        return (left * len(lista[:half]) + right * len(lista[half:])) / len(lista)


def zad2():
    l = list((input('Podaj ciąg liczb: ')))
    #print(f'1 i 2 maksymalny element w liście: {max_element2(l, l[0], l[1])}')
    print(f'1 i 2 maksymalny element w liście: {max_num(l), second_max_num(l)}')
    print(f'Średnia liczb na liście: {mean2(l)}')

print(f'\nzadanie2')
zad2()

# zadanie 3

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    half = len(lista) // 2
    left = merge_sort(lista[:half])
    right = merge_sort(lista[half:])

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Dodanie pozostałych elementów z lewej i prawej listy, jeśli istnieją
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def zad3():
    l = list((input('Podaj ciąg liczb do sortowania: ')))
    print(merge_sort(l))

print(f'\nzadanie 3 ')
zad3()

# Zadanie 4

def load_file(file_name='edges.json'):
    f = open(file_name)
    data = json.load(f)
    return data

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        G = nx.Graph()
        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold', width=2)
        plt.title("Graph")
        plt.show()

    def shortest_path(self, start, end, visited=None):
        if visited is None:
            visited = set()

        if end in self.adj_list[start]:
            return [start, end], 1

        visited.add(start)
        shortest = None

        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                path, length = self.shortest_path(neighbor, end, visited.copy())
                if path is not None and (shortest is None or length + 1 < len(shortest)):
                    shortest = [start] + path
                    length += 1

        return shortest, len(shortest) - 1 if shortest is not None else float('inf')

def add_edges(graph):
    edges = load_file()
    for _, value in edges.items():
        edge = [int(x) for x in value.split(',')]
        graph.add_edge(edge[0], edge[1])

g = Graph()
add_edges(g)

start_vertex = 1
end_vertex = 5
path, length = g.shortest_path(start_vertex, end_vertex)
if path:
    print("\nNajkrótsza ścieżka:", path)
    print("Długość najkrótszej ścieżki:", length)
else:
    print("Brak ścieżki między wierzchołkami", start_vertex, "i", end_vertex)
g.display()


# ZADANIE 5
def measure_time(func, data):
    start_time = time.time()
    func(data)
    return time.time() - start_time


sizes = [10, 100, 1000, 10000]
times_max_num = []
times_mean = []
times_merge_sort = []


for size in sizes:
    data = np.random.randint(0, 1000, size=size)
    times_max_num.append(measure_time(max_num2, data))
    times_mean.append(measure_time(mean2, data))
    times_merge_sort.append(measure_time(merge_sort, data))


fig, ax = plt.subplots(2,2)

ax[0,0].plot(sizes, times_max_num, label='Dwa największe elementy na liście')
ax[0,0].plot(sizes, times_mean, label='Średnia')
ax[0,0].set_xlabel('Rozmiar danych wejściowych')
ax[0,0].set_ylabel('Czas wykonania (s)')
ax[0,0].set_title('Wykres czasu działania algorytmów z zadania nr 2')
ax[0,0].legend()

ax[0,1].plot(sizes, times_merge_sort, label='Sortowanie przez scalanie')
ax[0,1].set_xlabel('Rozmiar danych wejściowych')
ax[0,1].set_ylabel('Czas wykonania (s)')
ax[0,1].set_title('Wykres czasu działania algorytmu z zadania nr 3')
ax[0,1].legend()

ax[1,1].remove()

ax[1,0].plot(sizes, times_merge_sort, label='Sortowanie przez scalanie')
ax[1,0].plot(sizes, times_max_num, label='Dwa największe elementy na liście')
ax[1,0].plot(sizes, times_mean, label='Średnia')
ax[1,0].set_xlabel('Rozmiar danych wejściowych')
ax[1,0].set_ylabel('Czas wykonania (s)')
ax[1,0].set_title('Porównanie działania wszystkich algorytmów')
ax[1,0].legend()
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()