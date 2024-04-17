#Antoni Smółka
from zad4testy import runtests

#definiuje algorytm przeszukujacy graf w szerz (BFS)
def bfs(G, s, t):
    visited = [False] * len(G)  
    prev = [None] * len(G)
    queue = [s]
    visited[s] = True

#tworze 4 tablice, z czego jedna bedzie kolejką


    while queue:
        node = queue.pop(0)
        if node == t:
            break

        for neighbor in G[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                prev[neighbor] = node
                queue.append(neighbor)

    path = []
    if not visited[t]:
        return None

    current = t
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return path

    #algorytm zwraca najkrotsza sciezke przedstawiona przy pomocy wierzcholkow pomiedzy s i t

def longer( G, s, t ):
    path = bfs(G, s, t)
    if not path:
        return None

    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]

        # usuwam krawędź uv z grafu
        G[u].remove(v)
        G[v].remove(u)

        # ponownie stostuje bfs zeby sprawdzic czy mimo usuniecia krawedzi istnieje sciezka 
        # nowa zmienna zawiera sciezke w grafie z usunieta krawedzia
        new_path = bfs(G, s, t)

        #porownuje czy sciezka po usunieciu krawedzi jest dluzsza od sciezki w grafie pierwotnym, jesli tak to zwracam usunieta krawedz

        if not new_path or len(new_path) > len(path):
            return (u, v)

    return None

   


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )


#złozonosc to O(V(V+E)) - V+E zlozonosc BFSa a V to zlozonosc petli for w funkcji longer(w najgorszym wypadku przechodzi przez wszystkie wierzcholki i wtedy wynosi V)
