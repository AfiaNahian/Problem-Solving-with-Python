t= int(input())
for i in range (t):
    w,x,y,z = input().split()
    w = int(w)
    x = int(x)
    y = float(y)
    z = float(z)
    c=0
    while(w<=x):
        c1=int((w*y)/100)
        c2=int((x*z)/100)

        w+=c1
        x+=c2
        c+=1
        if(c>100):
            break
    if(c>100):
        print(f"Mais de 1 seculo.")
    else:
        print(f"{c} anos.")