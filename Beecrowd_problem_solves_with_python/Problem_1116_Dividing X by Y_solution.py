t = int(input())
for i in range (t):
    nums = input().split(" ")
    a , b = nums
    a = int(a)
    b = int(b)
    if(b==0):
        print("divisao impossivel")
    else:
        r = a/b
        r ="{:.1f}".format(r)
        print(r)