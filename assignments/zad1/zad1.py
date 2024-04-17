from zad1testy import runtests

# Algorytm przechodzi po każdej literze stringa i liczy ile jest identycznych znaków po lewej i prawej od danej litery.

def ceasar(s):
    w=0
    for i in range(0,len(s)):
        k=1
        while i-k>=0 and i+k<=len(s)-1:
            if s[i-k]==s[i+k]:
                k+=1
            else:
                break
        if w<k:
            w=k
                
    return 2*w-1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )



