pos=0
total=0
for i in range (1,7):
    a=float(input())
    if(a>0):
        pos+=1
        total+=a

pre_total="{:.1f}".format(total/pos)
print("{} valores positivos".format(pos))
print(pre_total)