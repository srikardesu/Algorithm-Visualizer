

visited = set()

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return

if __name__ == "__main__":
    graph = {
        1: [2, 3, 4, 5],
        2: [1, 3],
        3: [1, 2, 4, 6],
        4: [1, 3, 5, 6],
        5: [1, 4, 6],
        6: [3, 4, 5]
    }

    # graph = {
    #     5 : [3, 7],
    #     3 : [2, 4],
    #     7 : [8],
    #     2 : [],
    #     4 : [8],
    #     8 : []
    # }

    x = int(input("Enter source node: "))
    if x not in graph.keys() :
        print("The node is not present in the garph :( .")
    else :
        print("The dfs is as follows: ")
        dfs(visited,graph,x)                  # gives the sequence that the nodes are visited during the dfs