from collections import deque


# Works with directed/undirected and connected/disconnected graphs

def bfs(G):
    n = len(G)
    parents = [None] * n
    visited = [False] * n

    for v in range(0, n):
        if not visited[v]:
            queue = deque([v])
            visited[v] = True

            while len(queue) > 0:
                vertex = queue.popleft()
                for neighbor in G[vertex]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parents[neighbor] = vertex
                        queue.append(neighbor)

    return parents, visited


def main():
    G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    print(bfs(G))


if __name__ == "__main__":
    main()
