from zad8testy import runtests
from collections import deque


def bfs(T, i, j):
    a = len(T)
    b = len(T[0])
    total_sum = T[i][j]
    T[i][j] = 0
    queue = deque([(i, j)])

    while queue:
        r, c = queue.popleft()

        if r - 1 > -1 and T[r - 1][c] != 0:
            total_sum += T[r - 1][c]
            T[r - 1][c] = 0
            queue.append((r - 1, c))

        if c - 1 > -1 and T[r][c - 1] != 0:
            total_sum += T[r][c - 1]
            T[r][c - 1] = 0
            queue.append((r, c - 1))

        if r + 1 < a and T[r + 1][c] != 0:
            total_sum += T[r + 1][c]
            T[r + 1][c] = 0
            queue.append((r + 1, c))

        if c + 1 < b and T[r][c + 1] != 0:
            total_sum += T[r][c + 1]
            T[r][c + 1] = 0
            queue.append((r, c + 1))

    T[i][j] = total_sum


def convert(T):
    for i in range(0, len(T[0])):
        if T[0][i] != 0:
            bfs(T, 0, i)

    return T[0]


def f(F, T, d, e):
    n = len(T) - 1
    i = n - d

    if e + T[i] == 0:
        return None

    cache = []

    for k in range(1, e + T[i] + 1):
        if i + k > n:
            continue
        elif i + k == n:
            return 1
        elif e - k + T[i] >= d - k:
            cache.append(1)
        else:
            if F[d - k][e - k + T[i]] is not None:
                cache.append(F[d - k][e - k + T[i]])

    if cache:
        return min(cache) + 1


def plan(T):
    T = convert(T)

    if T[0] >= len(T) - 1:
        return 1
    
    F = [[]]
    n = len(T)

    for i in range(1, n):
        tmp = []
        for j in range(i):
            tmp.append(None)

        F.append(tmp)

    for i in range(1, len(T) - 1):
        for j in range(0, i):
            F[i][j] = f(F, T, i, j)

    return f(F, T, n - 1, 0)


t = [[3, 0, 0, 0, 2, 0, 0, 0, 0, 4, 0, 4],
     [2, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 5],
     [7, 0, 0, 3, 2, 2, 0, 0, 0, 6, 7, 8]]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
