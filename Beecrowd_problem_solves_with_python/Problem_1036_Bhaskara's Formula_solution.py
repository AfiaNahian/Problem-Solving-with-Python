import math
input_value = input().split(' ')
a,b,c=input_value
a=float(a)
b=float(b)
c=float(c)

d=b*b-4*a*c

if((d<0) or (a==0)):
    print("Impossivel calcular")
else :
    d=math.sqrt(d)
    root_1=(-b+d)/(2*a)
    root_2=(-b-d)/(2*a)
    precised_root1="{:.5f}".format(root_1)
    precised_root2="{:.5f}".format(root_2)
    print("R1 =",precised_root1)
    print("R2 =",precised_root2)