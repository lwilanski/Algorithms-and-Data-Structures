
def rec_knapsack(W, P, term, b, i=0, cw=0, cp=0):
    if i == len(W):
        return cp, term.copy()

    results = [(0, 0), (0, 0)]

    term[i] = 0
    results[0] = rec_knapsack(W, P, term, b, i + 1, cw, cp)

    if cw + W[i] <= b:
        term[i] = 1
        results[1] = rec_knapsack(W, P, term, b, i + 1, cw + W[i], cp + P[i])

    return max(results)


w = [7, 2, 1, 5, 4, 3, 12, 15]
p = [15, 40, 25, 70, 50, 40, 90, 35]
ter = [0 for _ in range(len(w))]
b = 20

print(rec_knapsack(w, p, ter, b))
