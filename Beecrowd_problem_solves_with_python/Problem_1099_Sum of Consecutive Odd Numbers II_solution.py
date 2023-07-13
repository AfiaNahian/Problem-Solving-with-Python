t = int(input())
for i in range(t):
    nums = input().split(' ')
    a , b = nums
    a = int(a)
    b = int(b)
    total = 0
    if(a>b):
        temp = a
        a = b
        b = temp
    for j in range (a+1,b):
        if(j%2 == 1):
            total +=j
    print(f"{total}")