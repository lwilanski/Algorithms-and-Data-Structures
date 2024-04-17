class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.f_party = []
        self.g_party = []

    def g(self):
        self.g_party = []
        max_party = 0

        for v in self.children:
            max_party += v.f()
            self.g_party += v.f_party

        return max_party

    def f(self):
        self.f_party = []
        max_party = 0

        for v in self.children:
            max_party += v.g()

        a = max_party + self.value
        b = self.g()

        if a > b:
            for v in self.children:
                self.f_party += v.g_party

            self.f_party.append(self)
            return a

        else:
            self.f_party = self.g_party
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
    result.append(node.value)

print(result, sum(result))
