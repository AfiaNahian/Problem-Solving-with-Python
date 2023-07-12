loc = 1
h = 0
for i in range (1,101):
    n=int(input())
    if(n>=h):
        h=n
        floc=loc
    loc+=1

print(h)
print(floc)