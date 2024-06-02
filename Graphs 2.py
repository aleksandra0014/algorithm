import networkx as nx
import matplotlib.pyplot as plt
import json

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['E'],
    'G': ['H'],
    'H': []
}


graph_json = json.dumps(graph, indent=4)
with open('graph.json', 'w') as file:
    file.write(graph_json)

def draw_graph(graph, visited_nodes=None):
    G = nx.Graph(graph)  # Tworzenie obiektu grafu
    pos = nx.spring_layout(G, seed=42)  # Układ węzłów grafu
    node_color = ['green' if node in visited_nodes else 'lightblue' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=2000, font_size=15)
    plt.show()

def read_json(filename):
    with open(filename, 'r') as file:
        graph = json.load(file)
        return graph

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    draw_graph(graph, visited)
    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited)
    return visited

def full_DFS(graph):
    visited = set()
    draw_graph(graph, visited)
    for node in graph:
        if node not in visited:
            DFS(graph, node, visited)
    return visited

def topological_sort_util(graph, v, visited, stack):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            topological_sort_util(graph, i, visited, stack)
    stack.append(v)

def topological_sort(graph):
    visited = {node: False for node in graph}
    stack = []
    for node in graph:
        if not visited[node]:
            topological_sort_util(graph, node, visited, stack)
    return stack[::-1]

def visualize_step(graph, sorted_nodes, step):
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G, seed=1)

    plt.figure()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
    nx.draw_networkx_nodes(G, pos, nodelist=[sorted_nodes[step]], node_color='red', node_size=2000)
    plt.title(f"Krok {step+1}: {sorted_nodes[step]}")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    g = read_json('graph.json')
    zad = int(input('Podaj numer zadania: '))
    if zad == 1:
        DFS(g, 'A', visited=None)
    elif zad == 2:
        full_DFS(g)
    elif zad == 5:
        pass
    elif zad == 4:
        sorted_nodes = topological_sort(g)
        print(sorted_nodes)
        for step in range(len(sorted_nodes)):
            visualize_step(g, sorted_nodes, step)
