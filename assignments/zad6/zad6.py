from zad6testy import runtests


def odwiert(G, vertex, visited, counter):
    real_max = 0
    empty = True
    if vertex == len(G) or counter == len(G):
        return counter
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            empty = False
            visited[neighbor] = True
            curr_max = odwiert(G, vertex + 1, visited, counter + 1)
            visited[neighbor] = False
            if curr_max == len(G):
                return curr_max
            elif curr_max > real_max:
                real_max = curr_max

    if empty:
        curr_max = odwiert(G, vertex + 1, visited, counter)
        if curr_max == len(G):
            return curr_max
        elif curr_max > real_max:
            real_max = curr_max

    return real_max


def binworker(M):
    counter = 0
    visited = [False] * len(M)

    return odwiert(M, 0, visited, counter)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)

# G = [[0, 1, 3], [2, 4], [0, 2], [3], [2, 3]]
# # print(binworker(G))