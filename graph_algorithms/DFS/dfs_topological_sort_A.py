# Graph is represented as two-dimensional list of neighbors
# We only consider directed acyclic graph

def dfs(G, ver, visited, result, time):
    visited[ver] = True

    for neighbor in G[ver]:
        if not visited[neighbor]:
            dfs(G, neighbor, visited, result, time + 1)

    result.append(ver)

    if time == 0:
        for i in range(0, len(visited)):
            if not visited[i]:
                dfs(G, i, visited, result, time+1)
        result.reverse()

    return result, visited


def main():
    G = [[1, 2], [], [1, 4], [], [3, 5], [], [4]]
    visited = [False] * len(G)
    result = []
    time = 0
    print(dfs(G, 2, visited, result, time))


if __name__ == "__main__":
    main()
