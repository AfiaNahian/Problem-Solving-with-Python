while(1):
    a=int(input())
    if(a==0):
        break
    elif(a%2==0):
        c=0
        r=0
        while(c!=5):
            r+=a
            a+=2
            c+=1
        print(f"{r}")
    else:
        c=0
        r=0
        b = a + 1
        while(c!=5):
            r+=b
            b+=2
            c+=1
        print(f"{r}")