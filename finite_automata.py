import networkx as nx
import matplotlib.pyplot as plt


class AutomatSkonczony4:
    def __init__(self, start, end):
        self.current_state = start
        self.acceptable_state = [end]
        self.gamma = {
                    '(q0, a)': 'q0',
                    '(q0, b)': 'q1',
                    '(q0, c)': 'q4',
                    '(q0, d)': 'q4',
                    '(q1, c)': 'q2',
                    '(q1, a)': 'q4',
                    '(q1, b)': 'q4',
                    '(q1, d)': 'q4',
                    '(q2, d)': 'q3',
                    '(q2, a)': 'q4',
                    '(q2, b)': 'q4',
                    '(q2, c)': 'q4',
                    '(q3, d)': 'q3',
                    '(q3, a)': 'q4',
                    '(q3, b)': 'q4',
                    '(q3, c)': 'q4',
                    '(q4, c)': 'q4',
                    '(q4, a)': 'q4',
                    '(q4, b)': 'q4',
                    '(q4, d)': 'q4'}
        self.history = [start]

    def process(self):
        string = input('Podaj ciąg wejściowy: ')
        for i in range(len(string)):
            new_state = self.gamma[f'({self.current_state}, {string[i]})']
            print(f'Wcześniejszy stan {self.current_state} -- otrzymane wejście {(string[i])} -- nowy stan {new_state}')
            self.current_state = new_state
            self.history.append(new_state)
        if self.current_state in self.acceptable_state:
            print('Automat skończył się z powodzeniem')
        else:
            print(f'Automat skończył się z niepowodzeniem, ponieważ skończyliśmy na {self.current_state} '
                  f'a zbiór stanów kończących to {self.acceptable_state}')
        print(self.history)


class Graph:
    def __init__(self):
        self.graph = None
        self.nodes = ['start', 'q0', 'q1', 'q2', 'q3', 'q4']
        self.edges_with_labels = {
            ('start', 'q0'): '',
            ('q0', 'q1'): 'b',
            ('q0', 'q0'): 'a',
            ('q0', 'q4'): 'c,d',
            ('q1', 'q4'): 'a,b,d',
            ('q1', 'q2'): 'c',
            ('q2', 'q4'): 'a,b,c',
            ('q2', 'q3'): 'd',
            ('q3', 'q3'): 'd',
            ('q3', 'q4'): 'a,b,c',
            ('q4', 'q4'): 'a,b,c,d',
        }

    def create_graph(self):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(self.nodes)
        for edge, label in self.edges_with_labels.items():
            self.graph.add_edge(edge[0], edge[1], label=label)

    def show_graph(self):
        pos = nx.circular_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12,
                font_weight='bold')

        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        nx.draw_networkx_nodes(self.graph, pos=pos, nodelist=['q3'],
                               node_size=1000, node_color='skyblue',
                               linewidths=4, edgecolors='black')

        plt.show()


if __name__ == '__main__':
    auts = AutomatSkonczony4('q0', 'q3')
    auts.process()
    g = Graph()
    g.create_graph()
    g.show_graph()
