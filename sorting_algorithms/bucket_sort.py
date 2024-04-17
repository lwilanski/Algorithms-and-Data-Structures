from insertion_sort import insertion_sort

def bucket_sort(T):
    arr=[]
    bnum=10
    for i in range(bnum):
        arr.append([])

    for e in T:
        x=int(bnum*e)
        arr[x].append(e)

    for l in arr:
        insertion_sort(l)

    k=0
    for l in arr:
        for v in l:
            T[k]=v
            k+=1

    return T

x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(bucket_sort(x))
