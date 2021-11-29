import networkx as nx
import matplotlib.pyplot as plt

def minedgeweight(G, edgeprocessed):
    min = 100000000  
    for i in [(u, v, edgedata['length']) for u, v, edgedata in G.edges( data = True) if 'length' in edgedata ]:
    	if edgeprocessed[i] == False and i[2] < min:
    		min = i[2]
    		min_edge = i
    return min_edge

def findRoot(parent, i):
    if parent[i] == i:
        return i
    return findRoot(parent, parent[i])

def union(parent, order, x, y):
    xRoot = findRoot(parent, x)
    yRoot = findRoot(parent, y)
    if order[xRoot] < order[yRoot]:
        parent[xRoot] = yRoot
    elif order[xRoot] > order[yRoot]:
        parent[yRoot] = xRoot
    else :
        parent[yRoot] = xRoot
        order[xRoot] += 1

def kruskals(G, pos):
	no_of_edges = len(G.edges())
	no_of_vertices = len(G.nodes()) 
	mst = []
	edgeprocessed = {}
	for i in [ (u, v, edgedata['length']) for u, v, edgedata in G.edges(data = True) if 'length' in edgedata ]:
		edgeprocessed[i] = False 
	parent = [None] * no_of_vertices
	order = [None] * no_of_vertices

	for v in range(no_of_vertices):
		parent[v] = v
		order[v] = 0

	while len(mst) < no_of_vertices-1 :
		curredge = minedgeweight(G, edgeprocessed)
		edgeprocessed[curredge] = True
		y = findRoot(parent, curredge[1])
		x = findRoot(parent, curredge[0])
		if x != y:
			mst.append(curredge)
			union(parent, order, x, y)
	for v in mst:
	 	if (v[0], v[1]) in G.edges():
	 		nx.draw_networkx_edges(G, pos, edgelist = [(v[0], v[1])], width = 2, alpha = 1, edge_color = 'b')
	return

def CreateGraph():
	G = nx.Graph()
	f = open('inp_kruskal.txt')
	n = int(f.readline())
	WeightMatrix = []
	for i in range(n):
		list1 = list(map(int, (f.readline()).split()))
		WeightMatrix.append(list1)

	for i in range(n) :
		for j in range(n)[i:] :
			if WeightMatrix[i][j] > 0 :
					G.add_edge(i, j, length = WeightMatrix[i][j]) 
	return G


def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  
	edge_labels = nx.get_edge_attributes(G, 'length')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11)
	return pos

if __name__ == "__main__":
	G = CreateGraph()
	pos = DrawGraph(G)
	kruskals(G, pos)
	plt.show()