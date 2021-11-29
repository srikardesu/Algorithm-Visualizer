import networkx as nx
import matplotlib.pyplot as plt


def minimumdist(dist, doneset, V):
    min = 100000000
    for vertex in range(V):
        if doneset[vertex] == False and dist[vertex] <= min:
            min = dist[vertex]
            min_index = vertex
    return min_index


def bellman(G, source, pos):
    V = len(G.nodes())
    dist = []
    parent = []
    for _ in range(V):
        parent.append(None)
    for i in range(V):
        dist.append(100000000)
    dist[source] = 0
    parent[source] = -1
    for count in range(V-1):
        for u, v, d in G.edges(data=True):
            if dist[u] + d['length'] < dist[v]:
                dist[v] = d['length'] + dist[u]
                parent[v] = u

    for v in range(V):
        if parent[v] != -1:
            if (parent[v], v) in G.edges():
                nx.draw_networkx_edges(
                    G, pos, edgelist=[(parent[v], v)], width=2, alpha=1, edge_color='b')
    return


def CreateGraph():
    G = nx.DiGraph()    
    f = open('inp_bellmanford.txt')
    n = int(f.readline())
    wtMatrix = []
    for i in range(n):
        list1 = list(map(int, (f.readline()).split()))
        wtMatrix.append(list1)
    source = int(f.readline())
    for i in range(n):
        for j in range(n):
            if wtMatrix[i][j] > 0:
                G.add_edge(i, j, length=wtMatrix[i][j])
    return G, source


def DrawGraph(G):
    pos = nx.spring_layout(G)
    # print(pos)
    nx.draw(G, pos, with_labels=True)
    edge_labels = dict([((u, v), distance['length'])
                       for u, v, distance in G.edges(data=True)])
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=10)
    return pos


if __name__ == "__main__":
    G, source = CreateGraph()
    pos = DrawGraph(G)
    bellman(G, source, pos)
    plt.show()
