# Works with directed graphs

# Silnie spójna składowa w grafie skierowanym, to taki podgraf pierwotnego grafu w którym
# pomiędzy dwoma dowolnymi wierzchołkami istnieje ścieżka.
# Jeżeli wszystkie silnie spójne składowe zamienimy na pojedyncze wierzchołki to
# otrzymamy graf silnie spójnych składowych który jest DAG-iem.

# Algorytm do znajdowania silnie spójnych składowych wykonuje kroki:
# - odpal DFS na grafie zapisując czasy przetworzenia dla wierzchołków
# - odwróć kierunek wszystkich krawędzi
# - odpal jeszcze raz DFS zaczynając od wierzchołków które miały największy czas przetworzenia
# i teraz wierzchołki odwiedzone w danym dfs visit tworzą silnie spójną składową

def dfs_visit_order(G, vertex, visited, order):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs_visit_order(G, neighbor, visited, order)
    order.append(vertex)


def reverse_directions(G):
    result = []
    for i in range(0, len(G)):
        result.append([])

    for vertex in range(0, len(G)):
        while G[vertex]:
            tmp = G[vertex].pop()
            result[tmp].append(vertex)

    return result


def dfs_scc(G, visited):
    result = []
    order = []
    for v in range(0, len(G)):
        if not visited[v]:
            dfs_visit_order(G, v, visited, order)

    order.reverse()

    G = reverse_directions(G)

    visited = [False] * len(G)

    for v in order:
        scc = []
        if not visited[v]:
            dfs_visit_order(G, v, visited, scc)
            result.append(scc)

    return result


def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    visited = [False] * len(G)
    print(dfs_scc(G, visited))


if __name__ == "__main__":
    main()
