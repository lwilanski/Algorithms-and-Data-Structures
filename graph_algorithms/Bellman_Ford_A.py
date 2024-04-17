

def bellman_ford(G, s):
    parents = [None] * len(G)
    times = [None] * len(G)
    times[s] = 0

    for i in range(len(G)):
        change = False
        for vertex in range(0, len(G)):
            for neighbor, weight in G[vertex]:
                if times[neighbor] is None or times[neighbor] > times[vertex] + weight:
                    times[neighbor] = times[vertex] + weight
                    parents[neighbor] = vertex
                    change = True

        if not change:
            break

    if change:
        return None

    return times, parents


def main():
    G = [[(1, 8), (5, 10)], [(2, 1)], [(3, -1), (5, -4)], [(4, -2)], [(5, 1)], [(3, 2)]]
    print(bellman_ford(G, 0))


if __name__ == "__main__":
    main()
