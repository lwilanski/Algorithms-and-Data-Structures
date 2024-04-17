import random

# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać na prom.
# Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który wyznacza, które
# samochody powinny wjechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdzać w takiej kolejności, w jakiej są podane w tablicy A.

cars = []

cars0 = [2, 3, 5]
length0 = 5

cars1 = [3, 4, 3, 7, 3]
length1 = 10

cars2 = [4, 5, 7, 2, 3, 6, 4, 8]
length2 = 20

cars3 = [3, 2, 3, 1, 4, 2]
length3 = 30

cars.append((cars1, length1))
cars.append((cars2, length2))
cars.append((cars3, length3))
cars.append((cars0, length0))


def ver(A, L, left=0, right=0, c_car=0):
    cl = (left + A[c_car] <= L)
    cr = (right + A[c_car] <= L)

    if not cl and not cr:
        return c_car

    if (cr or cl) and c_car == len(A) - 1:
        return c_car + 1

    a = float('-inf')
    b = float('-inf')

    if cl:
        a = ver(A, L, left + A[c_car], right, c_car + 1)

    if cr:
        b = ver(A, L, left, right + A[c_car], c_car + 1)

    return max(a, b)


# Algorytm dynamiczny opiera się o funkcję f(i, s), która oznacza maksymalną liczbę aut, które mogą wjechać
# na prom jeśli, znajdują się na nim auta 0, ... , i oraz zajmują s miejsca na lewym pasie.

# f(i, s) = max( f(i + 1, s + A[i + 1]) + 1, f(i + 1, s) + 1, i ), gdzie warunkiem brzegowym jest
# f(i, s) = -inf jeśli s >= L (nie może wjechać na lewy) lub sum(A[:i + 1]) - s >= L (nie może wjechać na prawy)

# Implementacja 1: Zwykła rekurencja bez spamiętywania

def f_rec(A, L, i, s):
    if s > L or sum(A[:i + 1]) - s > L:
        return float('-inf')

    if i == len(A) - 1:
        return i + 1

    else:
        return max(f_rec(A, L, i + 1, s + A[i + 1]), f_rec(A, L, i + 1, s), i + 1)


def f_rec2(A, L, i, s, k=''):
    if s > L or sum(A[:i + 1]) - s > L:
        return float('-inf')

    if i == len(A) - 1:
        print(k)
        return i + 1

    else:
        return max(f_rec2(A, L, i + 1, s + A[i + 1], k + 'L'), f_rec2(A, L, i + 1, s, k + 'R'), i + 1)


# Implementacja 2: Rekurencja ze spamiętywaniem

def f_rec_mem(A, L, i, s, cache):
    if s > L or sum(A[:i + 1]) - s > L:
        return float('-inf')

    if cache[i][s] is not None:
        return cache[i][s]

    if i == len(A) - 1:
        cache[i][s] = i + 1
        return i + 1

    else:
        result = max(f_rec_mem(A, L, i + 1, s + A[i + 1], cache), f_rec_mem(A, L, i + 1, s, cache), i + 1)
        cache[i][s] = result
        return result


def rec_call(A, L):
    cache = [[None for _ in range(L + 1)] for _ in range(len(A))]

    return f_rec_mem(A, L, -1, 0, cache)


for i, t in enumerate(cars):
    # print("Cars:", i + 1)
    # print(ver(t[0], t[1]))
    # print(f_rec(t[0], t[1], -1, 0))
    # print(rec_call(t[0], t[1]))
    n = 40
    lower_bound = 1
    upper_bound = 1000
    lst = [random.randint(lower_bound, upper_bound) for _ in range(n)]
    long = random.randint(sum(lst) // 4, sum(lst) // 2)
    print(rec_call(lst, long))
    # print(ver(lst, long))
    # print(f_rec(lst, long, -1, 0))
    print('\n')
