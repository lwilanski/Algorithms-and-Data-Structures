from random_perm import permutation

def counting_sort(A,k):
    n=len(A)
    C=[0 for _ in range(k)]
    B=[0 for _ in range(n)]

    for e in A:
        C[e]+=1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]

    for j in range(n-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]-=1
        
    return B

        

t=permutation(20)
for i in range(0, len(t)):
    t[i]-=1
print(t)
print(counting_sort(t,20))

