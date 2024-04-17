from random_perm import permutation

def partition(T,start,end):
    pivot=T[end]
    g=start
    for i in range(start,end):
        if T[i]<pivot:
            T[i],T[g]=T[g],T[i]
            g+=1
    T[g],T[end]=T[end],T[g]
    return g

def quick_sort(T,p,q):
    if p<q:
        g=partition(T,p,q)
        quick_sort(T,p,g-1)
        quick_sort(T,g+1,q)
        
t=['beton','antoni','ciecierzyca']
print(t)
quick_sort(t,0,len(t)-1)
print(t)

    
    

            
    
