num =int(input())
for i in range(2,num+1):
    if(i%2==0):
        square=i*i
        print("{}^2 = {}".format(i,square))