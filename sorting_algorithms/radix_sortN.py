def count_sort(A, place):
    B = [0] * len(A)
    C = [0] * 10
    for e in A:
        x = e % (10 ** place) // (10 ** (place - 1))
        C[x] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for j in range(len(B) - 1, -1, -1):
        y = A[j] % (10 ** place) // (10 ** (place - 1))
        B[C[y] - 1] = A[j]
        C[y] -= 1
    A[:] = B[:]

def radix_sort(A):
    k=len(str(max(A)))
    for i in range(1,k+1):
        count_sort(A,i)

t = [100, 402, 615, 641, 758, 713, 632, 791, 887, 245, 147, 997, 496, 252, 123, 423, 734, 678, 123, 134]
radix_sort(t)
print(t)
