import heapq
from kol3btesty import runtests

def rebuild(G, A):
    for i in range(0, len(G)):
        for j in range(i+1, len(G)):
            found = False
            for k in range(0, len(G[i])):
                if G[i][k][0] == j:
                    if G[i][k][1] > A[i] + A[j]:
                        G[i][k] = (j, A[i] + A[j])
                        for v in range(0, len(G[j])):
                            if G[j][v][0] == i:
                                G[j][v] = (i, A[i] + A[j])
                                break
                    found = True
                    break
                
            if not found:
                G[i].append((j, A[i] + A[j]))
                G[j].append((i, A[i] + A[j]))
                                           
def dijkstra_shortest_path(G, s, t):
    visited = [False] * len(G)
    distances = [float('inf')] * len(G)
    distances[s] = 0
    parents = [None] * len(G)
    queue = [(0, s)]

    while queue:
        _, vertex = heapq.heappop(queue)

        if vertex == t:
            break

        if visited[vertex]:
            continue

        visited[vertex] = True

        for neighbor, weight in G[vertex]:
            new_distance = distances[vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = vertex
                heapq.heappush(queue, (new_distance, neighbor))

    return distances[t]
            
def airports(G, A, s, t):
    rebuild(G, A)
    return dijkstra_shortest_path(G, s, t)

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

