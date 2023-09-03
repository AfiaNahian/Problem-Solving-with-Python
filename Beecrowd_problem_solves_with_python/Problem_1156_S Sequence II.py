a=3
b=2
r=1
while(a!=39):
    #print(f"{a}/{b}")
    r+=(a/b)
    a+=2
    b*=2

r = "{:.2f}".format(r)
print(f"{r}")