# Struktura danych Union-Find, znana również jako struktura danych rozłącznych zbiorów,
# jest wykorzystywana do efektywnego śledzenia i zarządzania grupą
# elementów podzielonych na rozłączne (niezależne) zbiory.
#
# Ma dwa główne operacje:
#
# Find: Ta operacja zwraca identyfikator zbioru, do którego należy element.
# Elementy, które są w tym samym zbiorze, mają ten sam identyfikator.
# W tej implementacji identyfikatorem jest korzeń drzewa reprezentującego zbiór.
# Operacja "find" jest optymalizowana za pomocą techniki zwanej ścieżką kompresji, co oznacza,
# że każde wywołanie "find" dla danego elementu uaktualnia rodzica tego elementu do korzenia zbioru.
#
# Union: Ta operacja łączy dwa zbiory w jeden. Wybiera korzeń jednego z drzew (reprezentującego zbiór) i
# dołącza go do korzenia drugiego drzewa. W Twojej implementacji jest to zrealizowane z uwzględnieniem rangi drzew,
# co oznacza, że drzewo o mniejszej randze jest zawsze dołączane do drzewa o większej randze.
# Dzięki temu zachowana jest zbalansowana struktura drzewa, co poprawia efektywność operacji "find".
#
# Kod, który podałeś, działa zgodnie z tymi zasadami. Gdy tworzysz nową instancję UnionFind,
# każdy element jest własnym rodzicem (reprezentuje osobny zbiór), a ranga każdego elementu wynosi 0.
# Późniejsze wywołania "find" i "union" modyfikują te struktury danych w celu zarządzania zbiorami.


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

        return True
