a=1.0
r=0
for i in range (1,101):
    r+=(1/a)
    a+=1

r = "{:.2f}".format(r)
print(f"{r}")