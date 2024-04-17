from random_perm import permutation

def heapify(T,n,r):
    largest=r
    left=2*r+1
    right=2*r+2
    
    if left<n and T[left]>T[largest]:
        largest=left

    if right<n and T[right]>T[largest]:
        largest=right

    if largest!=r:
        T[r],T[largest]=T[largest],T[r]
        heapify(T,n,largest)

def heap_sort(T):
    n=len(T)
    for i in range(n//2-1,-1,-1):
        heapify(T,n,i)
        
    for j in range(n-1,0,-1):
        T[j],T[0]=T[0],T[j]
        heapify(T,j,0)

t=permutation(10)
print(t)
heap_sort(t)
print(t)
