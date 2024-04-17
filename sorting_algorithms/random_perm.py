import random as r

def permutation(n):
    T=[]
    for i in range(1,n+1):
        T.append(i)

    for i in range(0,len(T)):
        k=r.randint(i,len(T)-1)
        T[i],T[k]=T[k],T[i]

    return T


