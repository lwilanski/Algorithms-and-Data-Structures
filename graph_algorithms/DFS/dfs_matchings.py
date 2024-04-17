def dfs(G, vertex, match, visited):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if match[neighbor] == -1 or (not visited[match[neighbor]] and dfs(G, match[neighbor], match, visited)):
            match[neighbor] = vertex
            return True
    return False


def bin_worker(M):
    n = len(M)
    match = [-1] * n
    for v in range(n):
        dfs(M, v, match, [False] * n)

    return n - match.count(-1)
