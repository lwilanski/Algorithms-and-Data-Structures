def ceasar(s):
    w=0
    for i in range(0,len(s)):
        t=''
        for j in range(i,len(s)):
            t+=s[j]
            if t==t[::-1] and len(t)%2==1 and len(t)>w:
                w=len(t)
                
    return w

                      

            
        
