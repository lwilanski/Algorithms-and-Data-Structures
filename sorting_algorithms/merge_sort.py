from random_perm import permutation

def merge(A,B):
    W=[]
    i,j=0,0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            W.append(A[i])
            i+=1
        else:
            W.append(B[j])
            j+=1      
    W.extend(A[i:])
    W.extend(B[j:])
    return W

def merge_sort(T):
    mid=len(T)//2
    l=T[:mid]
    r=T[mid:]
    if len(l)>1:
        l=merge_sort(l)
    if len(r)>1:
        r=merge_sort(r)
    return(merge(l,r))

        
    
    

