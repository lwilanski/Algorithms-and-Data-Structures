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


def plan(T):
    T = convert(T)
    n = len(T)
    f = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        f[i][n - 1] = 1
        f[n - 1][i] = 0

    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if i + T[i] + j >= n - 1:
                f[i][j] = 1
                continue
            elif j == 0 and T[i] == 0:
                f[i][j] = float('inf')
                continue

            cache = []
            for k in range(1, j + T[i] + 1):
                if i + k < n and -1 < j - k + T[i] < n and f[i + k][j - k + T[i]] is not None:
                    cache.append(f[i + k][j - k + T[i]] + 1)

            f[i][j] = min(cache)

    return f[0][0]


t = [[3, 0, 0, 0, 2, 0, 0, 0, 0, 4, 0, 4],
     [2, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 5],
     [4, 0, 0, 3, 2, 2, 0, 0, 0, 6, 7, 8]]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)

