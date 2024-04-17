from random_perm import permutation

def shell_sort(T):
    gap=len(T)//2
    while gap>0:
        i=0
        while i+gap<len(T):
            j=i+gap
            while j<len(T):
                x=T[j]
                k=j-gap
                while k>-1 and x<T[k]:
                    T[k+gap]=T[k]
                    k-=gap
                T[k+gap]=x
                j+=gap
            i+=1
        gap=gap//2
            
                           
t=permutation(15)
print(t)
shell_sort(t)
print(t)
