
# Mamy drzewo które reprezentuje hierarchię w jakiejś firmie. Pracownicy są reprezentowani jako wierzchołki.
# Rodzic danego wierzchołka jest jego przełożonym a dzieci danego wierzchołka są jego podwładnymi.
# Korzeń drzewa nie ma przełożonego i jest najwyżej w hierarchi, a liście nie mają podwładnych i są najniżej.
# Dodatkowo każdy pracownik ma przydzielony współczynnik imprezowości, który mówi nam o tym jak odlotowa jest
# ta osoba na imprezach. Im wyższa suma współczynników wszystkich uczestników imprezy tym lepsza jest ta impreza.

# Zadanie polega na zorganizowaniu najlepszej możliwej imprezy. Jest jednak haczyk polegający na tym
# że na tej samej imprezie nie może się znaleźć pracownik i jego bezpośredni przełożony.

# Problem sprowadza się zatem do znalezienia zbioru wierzchołków niezależnych o największej sumie w danym drzewie.
# Zbiór wierzchołków niezależnych, to taki zbiór w którym żadne dwa wierzchołki nie są połączone krawędzią.

# W tej implementacji drzewo jest reprezentowane za pomocą klasy Node, czyli listy wiązanej w której każdy
# obiekt klasy jest wierzchołkiem, a jego atrybutami są m.in. współczynnik imprezowości oraz bezpośredni podwładni.

# Dodatkowo dla każdego wierzchołka zdefiniujemy funkcje f(node) oraz g(node) gdzie:

# f(node) = wartość najlepszej imprezy w drzewie którego korzeniem jest node
# g(node) = wartość najlepszej imprezy w drzewie którego korzeniem jest node, ale node na nią nie idzie

# UWAGA: Oznaczenie f([node.children]) lub g([node.children]) to suma wartości funkcji f/g dla wszystkich dzieci node

# f(node) = max(node.fun + g([node.children]), g(node)) (max z imprezy na którą node idzie i na którą nie idzie)
# g(node) = f([node.children]) (skoro node nie idzie, to liczymy sumę po najlepszych imprezach u jego dzieci)

# Funkcje f i g są zaimplementowane jako metody klasy Node.
# Jeżeli dla jakiegoś obiektu klasy Node zostanie wywołana funkcja f lub g to wartość tej funkcji
# jest zapamiętywana w atrybucie f_value lub g_value, a członkowie tej imprezy w tablicach f_party i g_party

class Node:
    def __init__(self, value):
        self.fun = value
        self.children = []
        self.f_value = None
        self.g_value = None
        self.f_party = []
        self.g_party = []

    def g(self):
        if self.g_value is not None:
            return self.g_value

        best_g = 0

        for v in self.children:
            best_g += v.f()
            self.g_party += v.f_party

        self.g_value = best_g
        return best_g

    def f(self):
        if self.f_value is not None:
            return self.f_value

        max_party = 0

        for v in self.children:
            max_party += v.g()

        a = max_party + self.fun
        b = self.g()

        if a > b:
            for v in self.children:
                self.f_party += v.g_party

            self.f_party.append(self)
            self.f_value = a
            return a

        else:
            self.f_party = self.g_party
            self.f_value = b
            return b


node1 = Node(50)
node2 = Node(10)
node3 = Node(20)
node4 = Node(1)
node5 = Node(18)
node6 = Node(5)
node7 = Node(23)
node8 = Node(21)
node9 = Node(17)
node10 = Node(1)
node11 = Node(2)
node12 = Node(25)
node13 = Node(36)
node14 = Node(7)
node15 = Node(18)
node16 = Node(1)
node17 = Node(5)
node18 = Node(1)
node19 = Node(1)
node20 = Node(1)
node21 = Node(100)
node22 = Node(100)
node23 = Node(100)

node1.children = [node2, node3, node4]
node2.children = [node5, node6, node7]
node3.children = [node8, node9]
node4.children = [node10, node11]
node5.children = [node12, node13, node14]
node8.children = [node15, node16, node17]
node10.children = [node18, node19]
node11.children = [node20]
node14.children = [node21, node22, node23]

print(node1.f())

result = []
for node in node1.f_party:
    result.append(node.fun)

print(result, sum(result))
