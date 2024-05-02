import networkx as nx
import matplotlib.pyplot as plt
import json

def tworzenie_pliku():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (5, 4), (5, 7), (7,6), (4, 6), (9, 8)])
    data = nx.node_link_data(G)

    with open("graf.json", "w") as f:
        json.dump(data, f, indent=4)

def odczyt_pliku_tworzenie_grafu(sciezka):
    with open(f'{sciezka}', "r") as f:
        data = json.load(f)

    G = nx.node_link_graph(data)
    nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=800, font_size=15)
    plt.show()
    return G


def znajdz_skladowe(g):
    skladowe = []
    zbiory_rozlaczne = []

    for i in g.nodes:
        zbiory_rozlaczne.append({i})

    for k in g.edges:
        w1, w2 = k
        set1 = None
        set2 = None

        for zbior in zbiory_rozlaczne:
            if w1 in zbior:
                set1 = zbior
                break
        for zbior in zbiory_rozlaczne:
            if w2 in zbior:
                set2 = zbior
                break

        if set1 != set2:
            set1.update(set2)
            zbiory_rozlaczne.remove(set2)

    for z in zbiory_rozlaczne:
        skladowe.append(list(z))

    return skladowe


G = odczyt_pliku_tworzenie_grafu('graf.json')
print(znajdz_skladowe(G))
