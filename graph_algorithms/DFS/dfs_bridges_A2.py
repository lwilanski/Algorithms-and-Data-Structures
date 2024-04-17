# Works with undirected connected graphs

# Algorytm szuka mostów korzystając z funkcji low(v), gdzie v to wierzchołek należący do G.
# Przy każdym wywołaniu dfs-a dla wierzchołka v, obliczamy też funkcję pomocniczą time(v), która
# oznacza głębokość rekurencji, a dla wierzchołka jest to tak naprawdę odległość od startowego wierzchołka.
# low(v) = min( time(v), low(dzieci v (ustawiamy przy back-trackingu), low(po krawędziach wstecznych))
# I jeżeli dla jakiegos wierzchołka low(v) == time(v) to jest to most

def dfs_bridges(G, vertex, visited, parents, lows, times, time, bridges):
    visited[vertex] = True
    times[vertex] = time
    time += 1
    lows[vertex] = times[vertex]

    for neighbor in G[vertex]:
        if not visited[neighbor]:
            parents[neighbor] = vertex
            dfs_bridges(G, neighbor, visited, parents, lows, times, time, bridges)

        if lows[neighbor] < lows[vertex] and parents[vertex] != neighbor:
            lows[vertex] = lows[neighbor]

    tmp = []
    if lows[vertex] == times[vertex] and parents[vertex] is not None:
        tmp.append(vertex)
        tmp.append(parents[vertex])
        bridges.append(tmp)

    return bridges


def dfs_bridges2(G, vertex, visited, parents, lows, times, bridges, time=0):
    visited[vertex] = True
    times[vertex] = time
    lows[vertex] = times[vertex]

    for neighbor in G[vertex]:
        if not visited[neighbor]:
            parents[neighbor] = vertex
            dfs_bridges2(G, neighbor, visited, parents, lows, times, bridges, time + 1)

        if lows[neighbor] < lows[vertex] and parents[vertex] != neighbor:
            lows[vertex] = lows[neighbor]

    tmp = []
    if lows[vertex] == times[vertex] and parents[vertex] is not None:
        tmp.append(vertex)
        tmp.append(parents[vertex])
        bridges.append(tmp)

    return bridges


def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    # G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    G = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3, 5], [4, 6, 7], [5, 7], [5, 6]]
    visited = [False] * len(G)
    parents = [None] * len(G)
    lows = [None] * len(G)
    times = [None] * len(G)

    bridges = []

    print(dfs_bridges2(G, 2, visited, parents, lows, times, bridges))


if __name__ == "__main__":
    main()
