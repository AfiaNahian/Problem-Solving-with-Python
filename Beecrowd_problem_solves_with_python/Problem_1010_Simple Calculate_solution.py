product1 = input().split(" ")
product2 = input().split(" ")

code1,unit1,price1 = product1
code2,unit2,price2 = product2

unit1=int(unit1)
unit2=int(unit2)
price1=float(price1)
price2=float(price2)

total = (unit1*price1) + (unit2*price2)
precised_total = "{:.2f}".format(total)
print("VALOR A PAGAR: R$",precised_total)