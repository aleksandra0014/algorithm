import matplotlib.pyplot as plt
import networkx as nx
import time

class MT:
    def __init__(self, start, accept, not_accept, gamma):
        self.start = start
        self.accept = accept
        self.not_accept = not_accept
        self.current_node = start
        self.gamma = gamma
        self.tape = [start]
        self.head = 0
        self.history = []

    def step(self):

        old_state = self.current_node
        if self.head + 1 == len(self.tape):
            self.tape.append('_')
            current_state = (self.current_node, '_')
        else:
            current_state = (self.current_node, self.tape[self.head + 1])
        new = self.gamma[current_state]
        self.current_node = new[0]
        self.tape[self.head + 1] = new[1]
        if new[2] == 'R':
            self.head += 1
            self.tape.remove(old_state)
            self.tape.insert(self.head, self.current_node)

        else:
            if self.head <= 0:
                self.tape.remove(old_state)
                self.tape.insert(self.head, self.current_node)
            else:
                self.head -= 1
                self.tape.remove(old_state)
                self.tape.insert(self.head, self.current_node)

        print(self.tape)
        self.history.append(self.current_node)

    def process(self):
        string = input('Podaj wejście: ')
        self.tape.extend(list(string))

        while self.current_node != self.accept and self.current_node != self.not_accept:
            self.step()
        print(f'Ostatni node: {self.current_node}')



class Graph:
    def __init__(self):
        self.graph = None
        self.nodes = ['start', 'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
        self.edges_with_labels = {
            ('start', 'q0'): '',
            ('q0', 'q1'): 'b -> R',
            ('q0', 'q2'): '0 -> 0/, R',
            ('q0', 'q3'): '1 -> 1/, R',
            ('q1', 'q1'): '0/, 1/ -> R',
            ('q1', 'qa'): '_ -> L',
            ('q1', 'qr'): '0, 1 -> L',
            ('q2', 'qr'): '_ -> R',
            ('q2', 'q2'): '0,1 -> R',
            ('q2', 'q4'): 'b -> R',
            ('q3', 'q3'): '0, 1 -> R',
            ('q3', 'qr'): '_ -> R',
            ('q3', 'q5'): 'b -> R',
            ('q4', 'q4'): '0/, 1/ -> R',
            ('q4', 'qr'): '_, 1 -> R',
            ('q4', 'q6'): '0 -> 0/, L',
            ('q5', 'q5'): '0/, 1/ -> R',
            ('q5', 'qr'): '_, 0 -> R',
            ('q5', 'q6'): '1 -> 1/, L',
            ('q6', 'q6'): '0/, 1/ -> L',
            ('q6', 'q7'): 'b -> L',
            ('q7', 'q7'): '0, 1 -> L',
            ('q7', 'q0'): '0/, 1/-> R',
        }

    def create_graph(self):
        self.graph = nx.DiGraph()
        self.graph.add_nodes_from(self.nodes)
        for edge, label in self.edges_with_labels.items():
            self.graph.add_edge(edge[0], edge[1], label=label)

    def show_graph(self, q):
        pos = nx.circular_layout(self.graph)
        node_colors = ['skyblue' if node != q else 'red' for node in self.graph.nodes()]
        nx.draw(self.graph, pos, with_labels=True, node_size=1000, node_color=node_colors, font_size=8,
                font_weight='bold')

        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=5)

        node_colors2 = ['skyblue' if node != q else 'red' for node in ['qa', 'qr']]

        nx.draw_networkx_nodes(self.graph, pos=pos, nodelist=['qa', 'qr'],
                               node_size=1000, node_color=node_colors2,
                               linewidths=4, edgecolors='black')

        plt.show()

    def series_of_graphs(self, nodes):
        for i in nodes:
            time.sleep(2)
            self.show_graph(i)


relacje1 = {('q0', 'a'): ['q1', 'a*', 'R'],
           ('q1', 'a/'): ['q1', 'a/', 'R'],
           ('q0', '_'): ['qr', '_', 'L'],
           ('q1', '_'): ['qa', '_', 'L'],
           ('q1', 'a'): ['q2', 'a', 'L'],
           ('q2', 'a/'): ['q2', 'a/', 'L'],
           ('q2', 'a*'): ['q3', 'a*', 'L'],
           ('q3', 'a/'): ['q3', 'a/', 'R'],
           ('q3', 'a'): ['q4', 'a', 'R'],
           ('q3', 'a*'): ['q4', 'a*', 'R'],
           ('q4', '_'): ['qr', '_', 'L'],
           ('q4', 'a/'): ['q4', 'a/', 'R'],
           ('q4', 'a'): ['q5', 'a/', 'R'],
           ('q5', 'a/'): ['q5', 'a/', 'R'],
           ('q5', '_'): ['qr', '_', 'L'],
           ('q3', '_'): ['q6', '_', 'L'],
           ('q5', 'a'): ['q3', 'a/', 'R'],
           ('q6', 'a'): ['q6', 'a', 'L'],
           ('q6', 'a/'): ['q6', 'a/', 'L'],
           ('q6', 'a*'): ['q1', 'a*', 'R']
           }

relacje2 = {('q0', 'b'): ['q1', 'b', 'R'],
            ('q0', '0'): ['q2', '0/', 'R'],
            ('q0', '1'): ['q3', '1/', 'R'],
            ('q1', '0/'): ['q1', '0/', 'R'],
            ('q1', '1/'): ['q1', '1/', 'R'],
            ('q1', '_'): ['qa', '_', 'L'],
            ('q1', '0'): ['qr', '0', 'R'],
            ('q1', '1'): ['qr', '1', 'L'],
            ('q2', '_'): ['qR', '_', 'R'],
            ('q2', '0'): ['q2', '0', 'R'],
            ('q2', '1'): ['q2', '1', 'R'],
            ('q2', 'b'): ['q4', 'b', 'R'],
            ('q3', '0'): ['q3', '0', 'R'],
            ('q3', '1'): ['q3', '1', 'R'],
            ('q3', '_'): ['qR', '_', 'R'],
            ('q3', 'b'): ['q5', 'b', 'R'],
            ('q4', '0/'): ['q4', '0/', 'R'],
            ('q4', '1/'): ['q4', '1/', 'R'],
            ('q4', '_'): ['qr', '_', 'R'],
            ('q4', '1'): ['qr', '_', 'R'],
            ('q4', '0'): ['q6', '0/', 'L'],
            ('q5', '_'): ['qr', '_', 'R'],
            ('q5', '0'): ['qr', '_', 'R'],
            ('q5', '1'): ['q6', '1/', 'L'],
            ('q5', '0/'): ['q5', '0/', 'R'],
            ('q5', '1/'): ['q5', '1/', 'R'],
            ('q6', '0/'): ['q6', '0/', 'L'],
            ('q6', '1/'): ['q6', '1/', 'L'],
            ('q6', 'b'): ['q7', 'b', 'L'],
            ('q7', '0'): ['q7', '0', 'L'],
            ('q7', '1'): ['q7', '1', 'L'],
            ('q7', '0/'): ['q0', '0/', 'R'],
            ('q7', '1/'): ['q0', '1/', 'R'],
            }

# zadanie 1
#maszyna1 = MT('q0', 'qa', 'qr', relacje1)
#maszyna1.process()

# zadanie 2
#maszyna2 = MT('q0', 'qa', 'qr', relacje2)
#maszyna2.process()
#g = Graph()
#g.create_graph()
#g.series_of_graphs(maszyna2.history)

relacje3 = {
    ('q0', 'x'): ['q1', 'x', 'R'],
    ('q0', '0'): ['q2', '-1', 'R'],
    ('q0', '1'): ['q2', '-1', 'R'],
    ('q1', '-1'): ['q1', '-1', 'R'],
    ('q1', '0'): ['qr', '0', 'R'],
    ('q1', '1'): ['qr', '1', 'R'],
    ('q1', 'x'): ['qr', 'x', 'R'],
    ('q1', '_'): ['qa', '_', 'R'],
    ('q2', '_'): ['qr', '_', 'R'],
    ('q2', 'x'): ['q3', 'x', 'R'],
    ('q2', '1'): ['q2', '1', 'R'],
    ('q2', '0'): ['q2', '0', 'R'],
    ('q3', '_'): ['qr', '_', 'R'],
    ('q3', '0'): ['q4', '-1', 'L'],
    ('q3', '1'): ['q4', '-1', 'L'],
    ('q3', '-1'): ['q3', '-1', 'R'],
    ('q3', 'x'): ['qr', 'x', 'R'],
    ('q4', 'x'): ['q5', 'x', 'L'],
    ('q4', '-1'): ['q4', '-1', 'L'],
    ('q5', '-1'): ['q0', '-1', 'R'],
    ('q5', '0'): ['q5', '0', 'L'],
    ('q5', '1'): ['q5', '1', 'L'],

}
#tm3 = MT('q0', 'qa', 'qr', relacje3)
#tm3.process()


# zadanie 5
relacje5 = {
    ('q0', '_'): ['qr', '_', 'L'],
    ('q0', ','): ['qr', ',', 'L'],
    ('q0', '}'): ['qr', '}', 'L'],
    ('q0', '_'): ['qr', '_', 'L'],
    ('q0', '{'): ['q1', '{', 'R'],
    ('q0', '0'): ['qr', '0', 'R'],
    ('q0', '1'): ['qr', '1', 'R'],
    ('q0', '2'): ['qr', '2', 'R'],
    ('q0', '3'): ['qr', '3', 'R'],
    ('q0', '4'): ['qr', '4', 'R'],
    ('q0', '5'): ['qr', '5', 'R'],
    ('q0', '6'): ['qr', '6', 'R'],
    ('q0', '7'): ['qr', '7', 'R'],
    ('q0', '8'): ['qr', '8', 'R'],
    ('q0', '9'): ['qr', '9', 'R'],
    ('q1', '_'): ['qr', '_', 'L'],
    ('q1', ','): ['qr', ',', 'L'],
    ('q1', '{'): ['qr', '_', 'L'],
    ('q1', '0'): ['qr', '0', 'L'],
    ('q1', '1'): ['q2', '1', 'R'],
    ('q1', '2'): ['q2', '2', 'R'],
    ('q1', '3'): ['q2', '3', 'R'],
    ('q1', '4'): ['q2', '4', 'R'],
    ('q1', '5'): ['q2', '5', 'R'],
    ('q1', '6'): ['q2', '6', 'R'],
    ('q1', '7'): ['q2', '7', 'R'],
    ('q1', '8'): ['q2', '8', 'R'],
    ('q1', '9'): ['q2', '9', 'R'],
    ('q1', '}'): ['qr', '}', 'L'],
    ('q2', ','): ['q1', ',', 'R'],
    ('q2', '_'): ['qr', '_', 'L'],
    ('q2', '{'): ['qr', '_', 'L'],
    ('q2', '0'): ['q2', '0', 'R'],
    ('q2', '1'): ['q2', '1', 'R'],
    ('q2', '2'): ['q2', '2', 'R'],
    ('q2', '3'): ['q2', '3', 'R'],
    ('q2', '4'): ['q2', '4', 'R'],
    ('q2', '5'): ['q2', '5', 'R'],
    ('q2', '6'): ['q2', '6', 'R'],
    ('q2', '7'): ['q2', '7', 'R'],
    ('q2', '8'): ['q2', '8', 'R'],
    ('q2', '9'): ['q2', '9', 'R'],
    ('q2', '}'): ['q3', '}', 'R'],
    ('q3', '}'): ['qr', '}', 'R'],
    ('q3', ','): ['qr', '_', 'R'],
    ('q3', '{'): ['qr', ',', 'R'],
    ('q3', '0'): ['qr', '_', 'R'],
    ('q3', '1'): ['qr', '_', 'R'],
    ('q3', '2'): ['qr', '_', 'R'],
    ('q3', '3'): ['qr', '_', 'R'],
    ('q3', '4'): ['qr', '_', 'R'],
    ('q3', '5'): ['qr', '_', 'R'],
    ('q3', '6'): ['qr', '_', 'R'],
    ('q3', '7'): ['qr', '_', 'R'],
    ('q3', '8'): ['qr', '_', 'R'],
    ('q3', '9'): ['qr', '_', 'R'],
    ('q3', '_'): ['qa', '_', 'R']
}

maszyna5 = MT('q0', 'qa', 'qr', relacje5)
maszyna5.process()
