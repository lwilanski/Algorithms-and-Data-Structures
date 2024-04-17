from random_perm import permutation

def insertion_sort(T):
    for i in range(1,len(T)):
        x=T[i]
        j=i-1
        while j>-1 and x<T[j]:
            T[j+1]=T[j]
            j-=1
        T[j+1]=x


    
    
    
