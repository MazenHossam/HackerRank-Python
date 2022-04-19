from collections import Counter
n = int(input())
av_sizes=input().split()

offers={}
cn = int(input())
for _ in range(cn):
    size, price = input().split()
    
    if size in av_sizes:
        av_sizes.remove(size)
        if offers.__contains__(size): offers[size] += int(price)
        else: offers[size] = int(price)
    
print (sum(offers.values()))
