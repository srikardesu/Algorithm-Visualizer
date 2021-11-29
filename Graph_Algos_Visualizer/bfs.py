from queue import Queue


def BFS(adj_list, start, end):
    vis = set()
    queue = Queue()
    queue.put(start)
    vis.add(start)
    parent = dict()
    parent[start] = None
    pf = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == end:
            pf = True
            break

        for next_node in adj_list[current_node]:
            if next_node not in vis:
                queue.put(next_node)
                parent[next_node] = current_node
                vis.add(next_node)

    path = []
    if pf:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    return path

def addEdge(graph,u,v):
    graph[u].append(v)


# main function
if __name__ == "__main__":
    graph = {
        1: [2, 3, 4, 5],
        2: [1, 3],
        3: [1, 2, 4, 6],
        4: [1, 3, 5, 6],
        5: [1, 4, 6],
        6: [3, 4, 5]
    }

    x = int(input("Enter source node: "))
    y = int(input("Enter destination node: "))
    
    path = BFS(graph, x, y)
    if(path == []) :
        print("No path found :(")
    else :
        print("One of the shortest paths between the specified nodes in the given graph is: ")
        print(path)
