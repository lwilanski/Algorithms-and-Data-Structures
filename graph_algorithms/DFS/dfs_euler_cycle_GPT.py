
# Ten algorytm korzysta z tego że cykl Eulera jest po prostu sumą cykli prostych, tzn. takich które nie przechodzą
# przez żaden wierzchołek więcej niż raz.
# Przechodzimy rekurencyjnie dfs-em po grafie, usuwając krawędzie.
# Jak trafimy na wierzchołek z którego nie mamy gdzie iść dodajemy go do cyklu.
# DFS dodaje krawędzie do cyklu podczas back-trackingu oryginalny cykl jakim podążał DFS będzie odwrócony.


def dfs_euler(G, vertex, euler_cycle):
    while G[vertex]:
        neighbor = G[vertex].pop()
        G[neighbor].remove(vertex)
        dfs_euler(G, neighbor, euler_cycle)

    euler_cycle.append(vertex)


def find_euler_cycle(G):
    euler_cycle = []
    dfs_euler(G, 0, euler_cycle)

    return euler_cycle[::-1]


def main():
    # G = [[1, 4], [0, 2], [1, 3, 4, 5], [2, 4], [0, 2, 3, 5], [2, 4]]
    # G = [[1, 2], [0, 2], [0,1]]
    # G = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]]
    G = [[4, 1], [0, 2], [1, 3, 5, 4], [2, 4], [2, 3, 5, 0], [2, 4]]
    euler_cycle = find_euler_cycle(G)
    print(euler_cycle)


if __name__ == "__main__":
    main()
