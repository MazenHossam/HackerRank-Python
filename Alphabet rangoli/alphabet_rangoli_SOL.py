import string
def print_rangoli(size):
    al=list(string.ascii_lowercase)
    h=size*2-1
    w=h*2-1
    
    for i in range(int(h/2)+1):
        tmp_string="-".join(al[size-1:-len(al)+size-2-i:-1] + al[size-i:size])
        print(tmp_string.center(w,'-'))
    
    for i in range(int(h/2)-1,-1,-1):
        tmp_string="-".join(al[size-1:-len(al)+size-2-i:-1] + al[size-i:size])
        print(tmp_string.center(w,'-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
