from collections import deque


def bfs_cycles(G):
    visited = [False] * len(G)
    parents = [None] * len(G)

    for s in range(len(G)):
        if not visited[s]:
            queue = deque([s])
            visited[s] = True

            while queue:
                vertex = queue.popleft()

                for neighbor in G[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parents[neighbor] = vertex
                        queue.append(neighbor)

                    elif parents[vertex] != neighbor:
                        return True

    return False
