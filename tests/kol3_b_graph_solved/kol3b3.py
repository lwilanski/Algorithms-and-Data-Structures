from kol3btesty import runtests
import heapq

def airports(G, A, s, t):
    n = len(G)
    cost = [float('inf')] * n
    cost[s] = 0
    queue = [(0, s)]

    while queue:
        current_cost, u = heapq.heappop(queue)
        if current_cost != cost[u]:
            continue
        for v, c in G[u]:
            # Przypadek 1: Kiedy lecimy bezpośrednio z u do v
            if cost[u] + c < cost[v]:
                cost[v] = cost[u] + c
                heapq.heappush(queue, (cost[v], v))

            # Przypadek 2: Kiedy lecimy szybowcem z u do v
            for w in range(n):
                if w != u and w != v and cost[u] + A[u] + A[w] < cost[w]:
                    cost[w] = cost[u] + A[u] + A[w]
                    heapq.heappush(queue, (cost[w], w))

    return cost[t] if cost[t] != float('inf') else -1

runtests( airports, all_tests = True )
