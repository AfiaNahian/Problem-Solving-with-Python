while (1):
    nums = input().split(' ')
    a , b = nums
    a = int(a)
    b = int(b)
    if(a == b):
        break
    elif (a>b):
        print("Decrescente")
    else:
        print("Crescente")
