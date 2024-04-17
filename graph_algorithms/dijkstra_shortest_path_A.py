import heapq


def dijkstra(G, s, t):
    visited = [False] * len(G)
    times = [None] * len(G)
    times[s] = 0
    parents = [None] * len(G)
    queue = [(0, s)]

    while queue:
        vertex = heapq.heappop(queue)[1]

        if visited[vertex]:
            continue

        if vertex == t:
            path = []
            tmp = t
            while tmp is not None:
                path.append(tmp)
                tmp = parents[tmp]

            return path[::-1]

        visited[vertex] = True

        for neighbor, weight in G[vertex]:
            if not visited[neighbor]:
                if times[neighbor] is None or times[neighbor] > times[vertex] + weight:
                    times[neighbor] = round(times[vertex] + weight, 2)
                    parents[neighbor] = vertex

            heapq.heappush(queue, (times[neighbor], neighbor))


def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    # G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    G = [[(1, 2), (2, 14), (3, 15), (4, 12)], [(0, 2), (2, 3), (6, 13)], [(0, 14), (1, 3), (6, 15), (7, 2)],
         [(0, 15), (4, 14), (7, 13), (8, 11)], [(0, 12), (3, 14)], [(6, 16), (9, 15)],
         [(1, 13), (2, 15), (5, 16), (7, 3), (9, 4)], [(2, 2), (3, 13), (6, 3), (8, 12), (9, 11)],
         [(3, 11), (7, 12), (9, 11)], [(5, 15), (6, 4), (7, 11), (8, 11)]]
    # G = [[(1, 2), (2, 99)], [(0, 2), (2, 2), (3, 99)], [(0, 99), (1, 2), (3, 2)], [(2, 2), (1, 99)]]
    # G = [[(1, 2), (2, 1)], [(0, 2), (2, 5)], [(0, 1), (1, 5)]]
    # G = [[(1, 0.2), (3, 3.1), (4, 1.7)], [(0, 0.2), (2, 4.2), (4, 1.1)], [(1, 4.2), (3, 0.1), (4, 8.4)], [(0, 3.1), (2, 0.1), (4, 0.3)], [(0, 1.7), (1, 1.1), (2, 8.4), (3, 0.3)]]

    print(dijkstra(G, 0, 5))


if __name__ == "__main__":
    main()
