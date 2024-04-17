from random_perm import permutation

def shell_sort(T):
    gap=len(T)//2
    while gap>0:
        j=gap
        while j<len(T):
            i=j-gap
            while i>=0:
                if T[i+gap]>T[i]:
                    break
                else:
                    T[i+gap],T[i]=T[i],T[i+gap]
                i-=gap
            j+=1
        gap=gap//2

t=[3,7,1,3,6,2,6,7,2,1]
print(t)
shell_sort(t)
print(t)
