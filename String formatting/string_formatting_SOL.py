def print_formatted(number):
    
    for i in range(1,number+1):
        print('{:>{pad2}}{:>{pad}}{:>{pad}}{:>{pad}}'.format(i,str(oct(i))[2:],(str(hex(i))[2:]).upper(),str(bin(i))[2:],pad=len(bin(number))-1,pad2=len(bin(number))-2))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
