import heapq
from kol3btesty import runtests

def smaller(a, b):
    if a > b:
        return b
    else:
        return a

def contains(lst, element):
    for tup in lst:
        if tup[0] == element:
            return (True, tup)
        
    return False
                                           
def airports(G, A, s, t):
    visited = [False] * len(G)
    distances = [float('inf')] * len(G)
    distances[s] = 0
    queue = [(0, s)]

    while queue:
        _, vertex = heapq.heappop(queue)

        if vertex == t:
            break

        if visited[vertex]:
            continue

        visited[vertex] = True

        for v in range(0, len(G)):
            if v != vertex:
                tup = contains(G[vertex], v)
                if tup:
                    new_distance = distances[vertex] + smaller(tup[1][1], A[vertex] + A[v])
                else:
                    new_distance = distances[vertex] + A[vertex] + A[v]
                    
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    heapq.heappush(queue, (new_distance, v))

    return distances[t]
            
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )

#G = [ [(1, 3), (3,2)],
      #[(0, 3), (2, 20)],
      #[(1, 20), (5, 1), (3, 6)],
      #[(0, 2), (2, 6), (4, 1)],
      #[(3, 1), (5, 7)],
      #[(4, 7), (2, 1)] ]

#A = [50, 100, 1, 20, 2, 70]

#print(airports(G, A, 0, 5))

