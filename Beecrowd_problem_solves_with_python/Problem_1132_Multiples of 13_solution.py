a = int(input())
b = int(input())
r = 0
if(a>b):
    temp = a
    a = b
    b = temp
for i in range(a,b+1):
    if(i % 13 != 0):
        r += i
print(r)