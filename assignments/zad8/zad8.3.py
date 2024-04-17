from zad8testy import runtests
from collections import deque


def print_mat(M):
    for row in M:
        print(row)


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
    if not d:
        return 0

    n = len(T) - 1
    i = n - d

    if d <= e + T[i]:
        return 1

    if e + T[i] == 0:
        return None

    cache = []

    for k in range(1, e + T[i] + 1):
        if i + k > n:
            continue
        elif e - k + T[i] >= d - k:
            cache.append(1)
        else:
            if F[d - k][e - k + T[i]] is not None:
                cache.append(F[d - k][e - k + T[i]])

    if cache:
        return min(cache) + 1


def plan(T):
    T = [3, 1, 2, 0, 0, 3, 0, 0, 2, 0, 0, 5, 0]
    F = []
    n = len(T)
    s = sum(T[:-1])
    for i in range(0, n):
        x = s - n + 1 + i
        row = []
        if x < i:
            for e in range(0, x + 1):
                row.append(f(F, T, i, e))

        else:
            for e in range(0, i):
                row.append(f(F, T, i, e))

        F.append(row)

    print_mat(F)

    return F[n - 1][0]


t = [[3, 0, 0, 0, 2, 0, 0, 0, 0, 4, 0, 4],
     [2, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 5],
     [7, 0, 0, 3, 2, 2, 0, 0, 0, 6, 7, 8]]

a = [1, 2, 3, 4, 5]

plan(t)

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(plan, all_tests=True)
