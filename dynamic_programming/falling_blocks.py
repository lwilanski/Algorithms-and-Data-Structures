# Każdy klocek to przedział postaci [a, b].
# Dany jest ciąg klocków [a1, b1], [a2, b2], ... , [an, bn].
# Klocki spadają na oś liczbową w kolejności podanej w ciągu.
# Proszę zaproponować algorytm, który oblicza, ile klocków należy usunąć z listy tak,
# żeby każdy kolejny spadający klocek mieścił się w całości w tym, który spadł tuż przed nim.

# W tym zadaniu będziemy szukać najdłuższego niekoniecznie spójnego malejącego podciągu.
# Wykorzystamy w tym celu funkcję f(i), która oznacza najdłuższy podciąg bloków, które
# mogą na siebie spaść, kończący się na bloku i.

# f(i) = max po wszystkich f(0 do i - 1), które dają się przedłużyć.
# Żeby podciąg f(j) mógł być przedłużony o klocek i, to A[j][0] >= A[i][0] oraz A[j][1] <= A[i][1].
# Warunek brzegowy f(0) = 1.

blocks = [(1, 10), (8, 11), (2, 9), (3, 8), (8, 9), (4, 7), (0, 9), (5, 6)]


def falling_blocks(A):
    n = len(A)
    f = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1

    return n - max(f)


print(falling_blocks(blocks))

