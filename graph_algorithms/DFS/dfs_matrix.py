# DFS for matrix representation

def dfs(G, vertex, visited, parents):
    visited[vertex] = True
    for neighbor in range(0, len(G)):
        if G[vertex][neighbor] and not visited[neighbor]:
            parents[neighbor] = vertex
            dfs(G, neighbor, visited, parents)

    return parents, visited


def main():
    G = [[0, 1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [1, 1, 1, 1, 0]]
    visited = [False] * len(G)
    parents = [None] * len(G)
    print(dfs(G, 0, visited, parents))


if __name__ == "__main__":
    main()
