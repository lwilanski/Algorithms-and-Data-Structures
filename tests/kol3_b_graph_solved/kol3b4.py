from kol3btesty import runtests
import heapq

def airports(G, A, s, t):
    n = len(G)
    # Tworzymy graf H z dodatkowymi krawędziami reprezentującymi przeloty szybowcem
    H = [[] for _ in range(n)]
    for u in range(n):
        for v, c in G[u]:
            H[u].append((v, c))
        for v in range(n):
            if v != u:
                H[u].append((v, A[u] + A[v]))
    cost = [float('inf')] * n
    cost[s] = 0
    queue = [(0, s)]
    while queue:
        current_cost, u = heapq.heappop(queue)
        if current_cost != cost[u]:
            continue
        for v, c in H[u]:
            if cost[u] + c < cost[v]:
                cost[v] = cost[u] + c
                heapq.heappush(queue, (cost[v], v))
    return cost[t] if cost[t] != float('inf') else -1

runtests( airports, all_tests = True )
