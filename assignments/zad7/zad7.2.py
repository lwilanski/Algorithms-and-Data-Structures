# Łukasz Wilański
from zad7testy import runtests


# Mój algorytm rekurencyjnie sprawdza wszystkie ścieżki z (0, 0) do (n - 1, n - 1) i wybiera najdłuższą.

def maze(L):
    n = len(L)
    visited = build_matrix(n)
    times = build_times(n)
    return travel(L, 0, 0, 0, visited, n, times)


def build_matrix(n):
    matrix = []
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append(False)

        matrix.append(tmp)

    return matrix


def build_times(n):
    matrix = []
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append(0)

        matrix.append(tmp)

    return matrix


def travel(L, x, y, counter, visited, n, times):
    visited[x][y] = True
    times[x][y] = counter

    if x == n - 1 and y == n - 1:
        return counter

    else:
        results = [-1, -1, -1]
        if x - 1 > -1 and not visited[x - 1][y] and L[x - 1][y] == "." and counter + 1 > times[x - 1][y]:
            results[0] = travel(L, x - 1, y, counter + 1, visited, n, times)
            visited[x - 1][y] = False

        if y + 1 < n and not visited[x][y + 1] and L[x][y + 1] == "." and counter + 1 > times[x][y + 1]:
            results[1] = travel(L, x, y + 1, counter + 1, visited, n, times)
            visited[x][y + 1] = False

        if x + 1 < n and not visited[x + 1][y] and L[x + 1][y] == "." and counter + 1 > times[x + 1][y]:
            results[2] = travel(L, x + 1, y, counter + 1, visited, n, times)
            visited[x + 1][y] = False

    return max(results)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
