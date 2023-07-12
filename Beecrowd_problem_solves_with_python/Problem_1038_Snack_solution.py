input_value = input().split(' ')
a,b= input_value
a=int(a)
b=int(b)
if(a==1) :
    x=b*4.00
elif(a==2) :
    x=b*4.50
elif(a==3) :
    x=b*5.00
elif(a==4) :
    x=b*2.00
elif(a==5) :
    x=b*1.50

precised_x="{:.2f}".format(x)
print("Total: R$",precised_x)