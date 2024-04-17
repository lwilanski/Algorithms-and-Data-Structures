#Łukasz Wilański
from zad4testy import runtests
from collections import deque

#Algorytm korzysta z funkcji znajdującej najkrótszą ścieżkę w grafie pomiędzy
#dwoma wierzchołkami, opartej na BFS. Następnie po kolei usuwa każdą krawędź
#w najkrótszej ścieżce i szuka najkrótszej ścieżki na nowo. Jeżeli najkrótsza
#ścieżka się wydłuży, zwraca wynikową krawędź.
#Złożoność bfs_shortest_path O(V+E), w najgorszym przypadku najkrótsza ścieżka
#będzie zawierała wszystkie krawędzie i funkcja longer przejdzie po wszystkich
#krawędziach czyli O(E*(V+E))

def bfs_shortest_path(G, s, t):
    visited = [False] * len(G)
    visited[s] = True
    queue = deque([(s, [s])])

    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in G[vertex]:
            if neighbor == t:
                return path + [neighbor]
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, path + [neighbor]))

    return None
            
def longer(G, s, t):
    path=bfs_shortest_path(G, s, t)

    if not path:
        return None

    for i in range(0, len(path)-1):
        u=path[i]
        v=path[i+1]

        G[u].remove(v)
        G[v].remove(u)

        new_path=bfs_shortest_path(G, s, t)

        G[u].append(v)
        G[v].append(u)

        if not new_path or len(new_path) > len(path):
            return (u, v)

    return None

        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
