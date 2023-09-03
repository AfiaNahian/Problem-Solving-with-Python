a= int(input())
while(1):
    b=int(input())
    if(b>a):
        break

r=0
c=0
for i  in range(b+1):
    r+=a
    a+=1
    c+=1
    if(r>b):
        break

print(f"{c}")