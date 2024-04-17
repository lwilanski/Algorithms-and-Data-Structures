# Works with directed/undirected and connected/disconnected graphs

def dfs_visit(G, vertex, visited, parents):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            parents[neighbor] = vertex
            dfs_visit(G, neighbor, visited, parents)


def dfs(G, visited, parents):
    for v in range(0, len(G)):
        if not visited[v]:
            dfs_visit(G, v, visited, parents)

    return visited, parents


def main():
    G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    visited = [False] * len(G)
    parents = [None] * len(G)
    print(dfs(G, visited, parents))


if __name__ == "__main__":
    main()
