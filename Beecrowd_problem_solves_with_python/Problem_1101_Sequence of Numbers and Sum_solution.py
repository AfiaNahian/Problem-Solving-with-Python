while (1):
    nums = input().split(' ')
    a , b = nums
    a = int(a)
    b = int(b)
    if(a<= 0 or b<=0):
        break
    total = 0
    if(a>b):
        temp = a
        a = b
        b = temp
    for i in range(a,b+1):
        total += i
        print(f"{i} ",end="")
    print(f"Sum={total}")