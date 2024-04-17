#Łukasz Wilański
from zad2testy import runtests
#zastosowałem algorytm sortowania merge sort
def snow(S):
    def merge_sort(T):
        mid=len(T)//2
        l=T[:mid]
        r=T[mid:]
        if len(l)>1:
            l=merge_sort(l)
        if len(r)>1:
            r=merge_sort(r)
        return(merge(l,r))
    
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
    
    wawoz=merge_sort(S)
    czas=0
    snieg=0
    
    for i in range(len(wawoz)-1,0,-1):
        if wawoz[i]-czas>0:
            snieg+=wawoz[i]-czas
        else:
            break
        czas+=1
            
    return snieg

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests = True)
