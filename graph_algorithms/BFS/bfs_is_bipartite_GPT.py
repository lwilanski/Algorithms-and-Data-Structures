from collections import deque


def bfs_is_bipartite(G, s):
    colors = [None] * len(G)
    queue = deque([s])
    colors[s] = False

    while queue:
        vertex = queue.popleft()
        for neighbor in G[vertex]:
            if colors[neighbor] is None:
                # Color it with alternate color
                colors[neighbor] = not colors[vertex]
                queue.append(neighbor)
            elif colors[neighbor] == colors[vertex]:
                # Same color, the graph is not bipartite
                return False

    return True
