from zad1testy import runtests

def ceasar(s):
    longest_len = 0
    
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            length = right - left + 1
            if length % 2 == 1 and length > longest_len:
                longest_len = length
            left -= 1
            right += 1
    
    return longest_len

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
input()


