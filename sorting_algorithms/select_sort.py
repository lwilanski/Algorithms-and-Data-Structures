from random_perm import permutation

def select_sort(T):
    n=0
    while n<len(T)-1:
        m=n+1
        for i in range(n,len(T)):
            if T[m]>T[i]:
                m=i
                
        T[n],T[m]=T[m],T[n]
        n+=1
        

t=permutation(25)
print(t)
select_sort(t)
print(t)
        
        
        
        
