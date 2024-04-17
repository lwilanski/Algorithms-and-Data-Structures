def dfs(G, vertex, visited, postorder=None):
    visited[vertex] = True

    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs(G, neighbor, visited, postorder)

    if postorder is not None:
        postorder.append(vertex)


def transpose_graph(G):
    GT = [[] for _ in range(len(G))]
    for vertex in range(len(G)):
        for neighbor in G[vertex]:
            GT[neighbor].append(vertex)
    return GT


def strongly_connected_components(G):
    visited = [False] * len(G)
    postorder = []

    for vertex in range(len(G)):
        if not visited[vertex]:
            dfs(G, vertex, visited, postorder)

    GT = transpose_graph(G)
    visited = [False] * len(G)
    scc_list = []

    for vertex in reversed(postorder):
        if not visited[vertex]:
            scc = []
            dfs(GT, vertex, visited, scc)
            scc_list.append(scc)

    return scc_list

def main():
    # G = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2], [5], [4], [7, 9], [6, 8], [7], [6, 10], [9, 11], [10]]
    G = [[1], [2], [0, 3], [4], [5, 8], [6, 10], [3], [8], [10], [8], [7, 9]]
    print(strongly_connected_components(G))


if __name__ == "__main__":
    main()