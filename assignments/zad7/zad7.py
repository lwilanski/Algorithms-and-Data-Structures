from zad7testy import runtests


def maze(L):
    n = len(L)
    visited = build_matrix(n)
    result = travel(L, 0, 0, '', visited, n)

    if result == '':
        return -1

    else:
        return result


def print_matrix(M):
    for row in M:
        print(row)


def build_matrix(n):
    matrix = []
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append(False)

        matrix.append(tmp)

    return matrix


def travel(L, x, y, counter, visited, n):
    visited[x][y] = True

    if x == n - 1 and y == n - 1:
        return counter

    else:
        results = ['', '', '']
        if x - 1 > -1 and not visited[x - 1][y] and L[x - 1][y] == ".":
            results[0] = travel(L, x - 1, y, counter + "G", visited, n)
            visited[x - 1][y] = False

        if y + 1 < n and not visited[x][y + 1] and L[x][y + 1] == ".":
            results[1] = travel(L, x, y + 1, counter + "P", visited, n)
            visited[x][y + 1] = False

        if x + 1 < n and not visited[x + 1][y] and L[x + 1][y] == ".":
            results[2] = travel(L, x + 1, y, counter + "D", visited, n)
            visited[x + 1][y] = False

    return max(results, key=len)


L = ["....", "..#.", "..#.", "...."]

vis = build_matrix(len(L))

# print(travel(L, 0, 0, '', vis, len(L)))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
