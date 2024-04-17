# Works with undirected connected graphs

time = 1


def dfs_bridges(G, vertex, visited, parents, lows, times):
    global time
    visited[vertex] = True
    times[vertex] = time
    time += 1
    lows[vertex] = times[vertex]

    for neighbor in G[vertex]:
        if not visited[neighbor]:
            parents[neighbor] = vertex
            dfs_bridges(G, neighbor, visited, parents, lows, times)

        if lows[neighbor] < lows[vertex] and parents[vertex] != neighbor:
            lows[vertex] = lows[neighbor]

    return times, lows


def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    # G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    G = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3, 5], [4, 6, 7], [5, 7], [5, 6]]
    visited = [False] * len(G)
    parents = [None] * len(G)
    lows = [None] * len(G)
    times = [None] * len(G)

    print(dfs_bridges(G, 2, visited, parents, lows, times))

    bridges = []
    for i in range(len(G)):
        tmp = []
        if times[i] == lows[i] and parents[i] is not None:
            tmp.append(i)
            tmp.append(parents[i])
            bridges.append(tmp)

    print(bridges)


if __name__ == "__main__":
    main()
