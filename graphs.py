import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def pytaj_uzyt():
    num = int(input('Podaj liczbę wierzchołków: '))
    ox_min = int(input('Podaj min osi OX: '))
    ox_max = int(input('Podaj max osi OX: '))
    oy_min = int(input('Podaj min osi OY: '))
    oy_max = int(input('Podaj max osi OY: '))
    r = int(input('Podaj promień okręgów: '))
    return num, ox_min, ox_max, oy_min, oy_max, r


num_nodes, ox_min, ox_max, oy_min, oy_max, r = pytaj_uzyt()


def check_circles(x1, y1, c, r):
    cross = False

    for i in c:
        x2 = i[0]
        y2 = i[1]
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        sum_radius = 2 * r
        if distance < sum_radius:
            cross = True

    return cross


def show_graph(c, r, gpos, gr):  # pokaż nody i te okrągi wokół nich
    plt.clf()
    nx.draw(gr, gpos, with_labels=True, node_color='green')
    for i in c:
        x, y = i[0], i[1]
        circle = Circle((x, y), radius=r, color='black', fill=False)
        plt.gca().add_patch(circle)
    plt.axis('equal')
    plt.pause(1)
    plt.show()


def position(ox_min, ox_max, oy_min, oy_max):
    x = np.random.uniform(ox_min, ox_max)
    y = np.random.uniform(oy_min, oy_max)
    return x, y


def main(num, ox_min, ox_max, oy_min, oy_max, r):
    graph = nx.Graph()
    gpos = {}
    VV = list(range(1, num + 1))

    for v in VV:
        i = 0
        while i < 10:
            last_gpos = gpos.copy()
            graph.add_node(v)
            x, y = position(ox_min, ox_max, oy_min, oy_max)
            gpos[v] = [x, y]
            circles = list(gpos.values())
            show_graph(circles, r, gpos, graph)
            if check_circles(x, y, last_gpos.values(), r) is False:
                break
            else:
                gpos.pop(v)
                graph.remove_node(v)
                show_graph(last_gpos.values(), r, last_gpos, graph)
            i += 1

        print(f'Podjęto {i} dodatkowych prób dodania wierzchołka {v}')
        if i >= 10:
            print(f'Podczas 10 prób nie udało się dodać wierzchołka, co powoduje skończenie funkcji.')
            break


main(num_nodes, ox_min, ox_max, oy_min, oy_max, r)

