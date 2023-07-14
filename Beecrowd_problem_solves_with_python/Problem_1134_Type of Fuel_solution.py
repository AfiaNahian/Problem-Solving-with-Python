al = 0
g = 0
d = 0
while(1):
    a = int(input())
    if(a == 4):
        break
    elif(a > 4):
        continue
    else:
        if(a == 1):
            al += 1
        if(a == 2):
            g += 1
        if(a == 3):
            d += 1

print(f"MUITO OBRIGADO\nAlcool: {al}\nGasolina: {g}\nDiesel: {d}")
