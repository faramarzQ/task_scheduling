import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

def show(tasks, edges):
        g = nx.DiGraph()
        g.add_nodes_from(range(0, len(tasks)))

        for item in edges:
            g.add_edge(item[0], item[1])

        options = {
            'node_size': 300,
            'width': 1,
            'arrowsize': 15,
        }
        nx.draw(g, with_labels=True, **options)
        plt.show()