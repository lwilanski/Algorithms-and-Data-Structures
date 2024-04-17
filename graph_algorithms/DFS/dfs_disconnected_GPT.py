def dfs(G, vertex, visited):
    visited[vertex] = True

    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs(G, neighbor, visited)

def dfs_disconnected(G):
    visited = [False] * len(G)

    for vertex in range(len(G)):
        if not visited[vertex]:
            dfs(G, vertex, visited)
