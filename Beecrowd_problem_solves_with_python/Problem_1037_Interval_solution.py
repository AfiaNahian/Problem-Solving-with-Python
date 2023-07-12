p = float(input())

if(p>=0) and (p<=25):
    print("Intervalo [0,25]")
elif(p>25) and (p<=50):
    print("Intervalo (25,50]")
elif(p>50) and (p<=75):
    print("Intervalo (50,75]")
elif(p>75) and (p<=100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")