# Proszę zaproponować algorytm dla dwuwymiarowej wersji dyskretnego problemu plecakowego.
# Mamy dany zbiór P = {p1, ..., pn} pozycji i dla każdej pozycji p[i] podane są trzy liczby:
# v(p[i]) - wartość pozycji
# w(p[i]) - waga przedmiotu
# h(p[i]) - wysokość elementu
# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga nie przekracza
# danej liczby W (całkowita waga) oraz łączna wysokość danej liczby H (całkowita wysokość)

# Funkcja rekurencyjna z jakiej skorzystamy to f(i, j, k) co będzie oznaczać najdroższy podzbiór
# przedmiotów ze zbioru {0, 1, ... , i}, przy maksymalnej ładowności j oraz maksymalnej wysokości k

# f(i, j, k) = max( f(i - 1, j, k), f(i - 1, j - w[i], k - h[i]) + v[i] )

def print_mat(M):
    for row in M:
        print(row)


def knapsack_2d(v, w, h, W, H):
    n = len(v)
    dp = [[[0 for _ in range(H + 1)] for _ in range(W + 1)] for _ in range(n)]

    for j in range(w[0], W + 1):
        for k in range(h[0], H + 1):
            dp[0][j][k] = 1

    for i in range(1, n):
        for j in range(0, W + 1):
            for k in range(0, H + 1):
                if j - w[i] > - 1 and k - h[i] > -1:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - w[i]][k - h[i]] + v[i])

                else:
                    dp[i][j][k] = dp[i - 1][j][k]

    return dp[n - 1][W][H]


weights = [7, 2, 1, 5, 4, 3, 12, 15]
heights = [7, 2, 1, 5, 4, 3, 12, 15]
prices = [15, 40, 25, 70, 50, 40, 90, 35]
max_w = 20
max_h = 20

print(knapsack_2d(prices, weights, heights, max_w, max_h))
