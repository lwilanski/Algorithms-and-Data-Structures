def count_sort(A, p):
    B = [0] * len(A)
    C = [0] * 26
    for e in A:
        x = ord(e[p]) - ord('a')
        C[x] += 1
    for i in range(1, 26):
        C[i] += C[i - 1]
    for j in range(len(B) - 1, -1, -1):
        x = ord(A[j][p]) - ord('a')
        B[C[x] - 1] = A[j]
        C[x] -= 1
    A[:] = B[:]


def radix_sort(A):
    k = len(A[0])
    for i in range(k - 1, -1, -1):
        count_sort(A, i)


t = ['gad', 'fad', 'ebe', 'azz', 'acb', 'aga', 'ybb', 'add']
radix_sort(t)
print(t)
