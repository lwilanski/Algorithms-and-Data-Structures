from zad1testy import runtests

def ceasar(s):
    max_dlugosc = 1
    g=0
    dlugosc = len(s)

    for i in range(0, dlugosc):
        # szukamy palindromów o nieparzystej długości, zaczynając od indeksu i
        for j in range(1, (dlugosc - i) // 2):
            if s[i-j] != s[i+j]:
                break
            else:
                palindrom_dlugosc = j * 2 + 1
                if palindrom_dlugosc > max_dlugosc:
                    max_dlugosc = palindrom_dlugosc
                    g=i

    return max_dlugosc, g

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( ceasar , all_tests = True )
x='uzozuestbofefobtseqkaitwqkuyxyukqwtiakq'
print(ceasar(x))

