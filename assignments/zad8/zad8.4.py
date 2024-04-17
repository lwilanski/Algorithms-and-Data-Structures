# Łukasz Wilański

# Algorytm najpierw sprowadza dwuwymiarową listę z plamami to jednowymiarowej listy (tak jak w problemie z głodną żabą)
# Następnie, jeżeli nie da się w jednym przejeździe dotrzeć do końca, to w pętli dokłada najoptymalniejsze tankowanie
# które jest dostępne w zasięgu cysterny zwiększąjąc tym samym zasięg. Jeżeli zasięg jest na tyle duży że można dojechać
# do końca, pętla się kończy i zwracany jest wynik.
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
    n = len(T) - 1
    steps = 1
    vol = T[0]
    T[0] = 0

    while vol < n:
        s = T[:vol + 1].copy()
        m = T.index(max(s))
        vol += T[m]
        T[m] = 0
        steps += 1

    return steps


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
