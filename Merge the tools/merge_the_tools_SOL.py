import textwrap
def merge_the_tools(string, k):
    #sub=textwrap.wrap(string,k)
    #sub=set(sub)
    #print (sub)
    #print(textwrap.fill(string,k))
    #print (textwrap.fill(string,k)[0])
    
    #for i in range(0,len(string),k):
        #print("".join(set(string[i:i+k])))
        #print("".join(set(string[i:i+k])))
        
    for i in range(0,len(string),k):
        st=string[i:i+k]
        used=""
        for i in st:
            if i not in used:
                used=used+i
        print(used)
