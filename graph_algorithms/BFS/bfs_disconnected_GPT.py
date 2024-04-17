from collections import deque


def bfs(G, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbor in G[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


def bfs_disconnected(G):
    visited = [False] * len(G)

    for vertex in range(len(G)):
        if not visited[vertex]:
            bfs(G, vertex, visited)
