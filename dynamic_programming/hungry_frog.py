# Żaba skacze po osi długości n, której pola są ponumerowane od 0 do n - 1.
# Żaba potrzebuje energii żeby wykonać jakikolwiek skok.
# Na niektórych polach osi są przekąski które dostarczają żabie energii.
# Jeżeli na jakimś polu jest przekąska, to na osi będzie to liczba naturalna
# która reprezentuje ile energii otrzyma żaba jeżeli skoczy na to pole.
# Żaba startuje z pola 0 i chce doskoczyć do pola n - 1 w jak najmniejszej ilości skoków.
# Zakładamy że żaba na starcie ma 0 energii, ale na polu 0 zawsze znajduje się jakaś przekąska.
# Zakładamy że rozwiązaie istnieje. Dane jakie otrzymujemy to lista z wartościami przekąsek.

t1 = [3, 1, 2, 0, 0, 3, 0, 0, 2, 0, 0, 5, 0]
t2 = [2, 5, 0, 2, 0, 0, 2, 0]


# Algorytm dynamiczny, implementuje funkcję f(i, j) która oznacza minimalną liczbę skoków niezbędną żeby
# dotrzeć do końca jeśli żaba stoi na polu i oraz ma j energii (energii z tego pola nie wliczamy do j).

# f(i, j) = min po wszystkich k, gdzie 1 <= k <= j + T[i] z wartości f(i + k, j + T[i] - k) + 1.
# Znajdujemy po prostu minimum ze wszystkich skoków jakie żaba może wykonać z pola i miejąc j energii.
# Rozwiązaniem w tym przypadku jest f(0, 0).
def hungry_frog(T):
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


print(hungry_frog(t1))
