import random


# Mamy n przedmiotów, którym przypisujemy wagi i ceny.
# Złodziej włamuje się do domu i chce ukraść jak najwięcej, ale jego plecak ma maksymalną ładowność B.
# Zadanie polega na znalezieniu najdroższego podzbioru przedmiotów którego łączna waga nie przekracza B.
# Wagi i ceny przedmiotów są reprezentowane jako dwie tablice o długości n, gdzie indeksy to numery przedmiotów.

# Wprowadzam oznaczenie W na tablicę z wagami, P na tablicę z cenami.
# f(i, b) - najdroższy podzbiór przedmiotów ze zbioru {0, ... , i}, przy maksymalnej ładowności b (nie większej niz B)

# Wartości funkcji f będziemy obliczać jako maksimum z dwóch przypadków. Bierzemy przedmiot i-ty lub nie.
# f(i, b) = max(f(i - 1, b - W[i]) + P[i], f(i - 1, b))
# Warunki brzegowe f(0, b) = 0 if W[0] > b else 1
# Wynikiem zadania będzie f(n - 1, B)

# Wartości funkcji będziemy przechowywać w tablicy dwuwymiarowej n x b, w której wiersze odpowiadają wagom [0, b],
# a kolumny odpowiadają przedmiotom [0, n - 1].

# Funkcja knapsack_1 oblicza wartości funkcji f idąc po wierszach, a knapsack_2 idąc po kolumnach
# Funkcja rec_knapsack jest rekurencyjną wersją algorytmu, bez programowania dynamicznego

def print_mat(M):
    for row in M:
        print(row)


# Implementacja 1: Algorytm dynamiczny który zapełnia tablicę z wartościami funkcji, WIERSZAMI od lewej do prawej

def knapsack_1(W, P, b):
    n = len(W)
    F = [[0 for _ in range(n)] for _ in range(b + 1)]

    for i in range(W[0], b + 1):
        F[i][0] = P[0]

    for row in range(0, b + 1):
        for col in range(1, n):
            if row - W[col] > -1:
                F[row][col] = max(F[row][col - 1], F[row - W[col]][col - 1] + P[col])
            else:
                F[row][col] = F[row][col - 1]

    return F[b][n - 1]


# Implementacja 2: Algorytm dynamiczny który zapełnia tablicę z wartościami funkcji, KOLUMNAMI z góry na dół

def knapsack_2(W, P, b):
    n = len(W)
    F = [[0 for _ in range(n)] for _ in range(b + 1)]

    for i in range(W[0], b + 1):
        F[i][0] = P[0]

    for col in range(1, n):
        for row in range(0, b + 1):
            if row - W[col] > -1:
                F[row][col] = max(F[row][col - 1], F[row - W[col]][col - 1] + P[col])
            else:
                F[row][col] = F[row][col - 1]

    return F[b][n - 1]


# Implementacja 3: Zwykły algorytm rekurencyjny

def rec_knapsack(W, P, b, i=0, cw=0, cp=0):
    if i == len(W):
        return cp

    results = [0, 0]

    results[0] = rec_knapsack(W, P, b, i + 1, cw, cp)

    if cw + W[i] <= b:
        results[1] = rec_knapsack(W, P, b, i + 1, cw + W[i], cp + P[i])

    return max(results)


w = [7, 2, 1, 5, 4, 3, 12, 15]
p = [15, 40, 25, 70, 50, 40, 90, 35]
b = 20
print(knapsack_2(w, p, b))

# n = 200
# lower_bound = 1
# upper_bound = 1000
# w = [random.randint(lower_bound, upper_bound) for _ in range(n)]
# p = [random.randint(lower_bound, upper_bound) for _ in range(n)]
# b = sum(w) // 2

# print(knapsack_1(w, p, b))
# print(knapsack_2(w, p, b))
