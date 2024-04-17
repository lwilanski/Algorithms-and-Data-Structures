from random_perm import permutation

def bubble_sort(T):
    n=len(T)-1
    while True:
        swapped=False
        for i in range(0,n):
            if T[i]>T[i+1]:
                T[i],T[i+1]=T[i+1],T[i]
                swapped=True
        n-=1
        if not swapped:
            break

t=permutation(40)
print(t)
bubble_sort(t)
print(t)

        
            
