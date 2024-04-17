from egz2btesty import runtests

# Algorytm tworzy tablicę dp o wymiarach n x m, w której oblicza kolejne
# wartości funkcji f(i, j) uwzględniając podane w zadaniu warunki.
# Algorytm działa w czasie m^3 ponieważ 1 raz przechodzimy tablicę dwuwymiarową dp w czasie m^2
# (ponieważ n może być równe m w najgorszym przypadku), ponadto dla każdej komórki dp[i][j]
# musimy znaleźć min z pierwszych j - 1 wartości dp[i - 1].


def parking(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]

    for i in range(m):
        dp[0][i] = abs(X[0] - Y[i])

    for i in range(1, n):
        for j in range(i, m):
            min_val = min(dp[i - 1][:j])
            dp[i][j] = min_val + abs(X[i] - Y[j])

    return min(dp[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)

x = [3, 6, 10, 14]
y = [1, 4, 5, 10, 11, 13, 17]

# print(parking(x, y))
