from collections import deque


def bfs_shortest_path(G, s, t):
    visited = [False] * len(G)
    queue = deque([((s, 1), [s])])

    while queue:
        print(queue)
        vertex, path = queue.popleft()

        if vertex[1] == 1:
            visited[vertex[0]] = True
            if vertex[0] == t:
                return path
            for neighbor in G[vertex[0]]:
                if not visited[neighbor[0]]:
                    queue.append((neighbor, path + [neighbor[0]]))
        else:
            queue.append(((vertex[0], vertex[1] - 1), path))

    return None


def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    # G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    # G = [[(1, 2), (2, 14), (3, 15), (4, 12)], [(0, 2), (2, 3), (6, 13)], [(0, 14), (1, 3), (6, 15), (7, 2)], [(0, 15), (4, 14), (7, 13), (8, 11)], [(0, 12), (3, 14)], [(6, 16), (9, 15)], [(1, 13), (2, 15), (5, 16), (7, 3), (9, 4)], [(2, 2), (3, 13), (6, 3), (8, 12), (9, 11)], [(3, 11), (7, 12), (9, 11)], [(5, 15), (6, 4), (7, 11), (8, 11)]]
    # G = [[(1, 2), (2, 99)], [(0, 2), (2, 2), (3, 99)], [(0, 99), (1, 2), (3, 2)], [(2, 2), (1, 99)]]
    G = [[(1, 2), (2, 1)], [(0, 2), (2, 5)], [(0, 1), (1, 5)]]

    print(bfs_shortest_path(G, 0, 2))


if __name__ == "__main__":
    main()
