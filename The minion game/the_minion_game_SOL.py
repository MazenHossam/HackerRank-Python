def minion_game(string):
    string=list(string)
    
    STUART=0
    KEVIN=0
    
    #con=[e for e in string if e not in ('A','O','U','I','E')]   # B N N 
    #vow=[e for e in string if e in ('A','O','U','I','E')]       # A A A
    
    for i in range(len(string)):
        if string[i] not in ('A','O','U','I','E'):
            STUART+= len(string)-i
        else:
            KEVIN+= len(string)-i
    
    if KEVIN>STUART: print("Kevin {}".format(KEVIN))
    elif KEVIN<STUART: print("Stuart {}".format(STUART))
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
