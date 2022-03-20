if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in range(N):
        op, *nums = input().split()
        nums = list(map(int, nums))
        
        if op=='insert':
            arr.insert(nums[0],nums[1])
        if op=='print':
            print(arr)
        if op=='remove':
            arr.remove(nums[0])
        if op=='append':
            arr.append(nums[0])
        if op=='sort':
            arr.sort()
        if op=='pop':
            arr.pop()
        if op=='reverse':
            arr.reverse()
