# Graph is represented as two-dimensional list of neighbors

# Algorytm DFS (przeszukiwanie w głąb) jest jednym z podstawowych algorytmów do przeszukiwania lub przeglądania grafów.
# DFS zaczyna od wybranego wierzchołka (lub wierzchołków), odwiedza jak najgłębiej możliwe wierzchołki,
# a następnie wraca wstecz, gdy osiągnie wierzchołek bez niesprawdzonych sąsiadów.

# Algorytm rozpoczyna od wierzchołka vertex i oznacza go jako odwiedzony (używając listy visited).

# Dla każdego nieodwiedzonego sąsiada tego wierzchołka, oznacza vertex jako
# rodzica tego sąsiada (używając listy parents) i rekurencyjnie wykonuje DFS na tym sąsiedzie.

# Proces ten kontynuowany jest aż do odwiedzenia wszystkich wierzchołków w grafie.

# Na końcu algorytmu zwracane są dwie listy: parents i visited.
# Lista parents zawiera informacje o drzewie DFS (czyli jakie wierzchołki są rodzicami innych wierzchołków),
# natomiast lista visited zawiera informacje, które wierzchołki zostały odwiedzone.


def dfs(G, vertex, visited, parents):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            parents[neighbor] = vertex
            dfs(G, neighbor, visited, parents)

    return parents, visited


# Explained version:

def dfse(G, vertex, visited, parents):
    # Mark the current node as visited.
    visited[vertex] = True
    # Go through all the adjacent nodes of the current node.
    for neighbor in G[vertex]:
        # If the neighbor node has not been visited yet...
        if not visited[neighbor]:
            # Mark the current node as the parent of the neighbor node.
            parents[neighbor] = vertex
            # Recursively apply DFS on the neighbor node.
            dfse(G, neighbor, visited, parents)
    # Return the parent and visited lists after the DFS traversal.
    return parents, visited


def main():
    # G = [[2], [2, 4], [0, 1, 3, 4], [2, 5], [1, 2], [3]]
    G = [[1, 4, 8], [0, 2, 3], [1, 5, 8], [1, 7], [0, 6, 8], [2, 6], [4, 5, 7], [3, 6], [0, 2, 4]]
    visited = [False] * len(G)
    parents = [None] * len(G)
    print(dfs(G, 0, visited, parents))


if __name__ == "__main__":
    main()
