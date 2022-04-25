N,M= input().split()
N=int(N)
M=int(M)

mirror=0
for i in range(N):
    if i<N/2-1:
        print ( ('.|.'*i).rjust(int(M/2-1),'-') +'.|.'+ ('.|.'*i).ljust(int(M/2-1),'-') )
    elif i==int(N/2):
        print( 'WELCOME'.center(M,'-') )
        mirror=i-1
    else:
        print ( ('.|.'*mirror).rjust(int(M/2-1),'-') +'.|.'+ ('.|.'*mirror).ljust(int(M/2-1),'-') )
        mirror-=1
