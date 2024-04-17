def dfs(G, start):
    visited = [False] * len(G)
    parents = [None] * len(G)
    stack = [start]

    while stack:
        vertex = stack.pop()

        if visited[vertex]:
            continue

        visited[vertex] = True

        for neighbor in G[vertex]:
            if not visited[neighbor]:
                parents[neighbor] = vertex
                stack.append(neighbor)

    return parents, visited


def main():
    G1 = [[1, 4], [0, 4], [3, 4], [2, 4], [0, 1, 2, 3]]
    G2 = [[4, 1], [4, 0], [4, 3], [4, 2], [3, 2, 1, 0]]

    print(dfs(G1, 0))


if __name__ == "__main__":
    main()
