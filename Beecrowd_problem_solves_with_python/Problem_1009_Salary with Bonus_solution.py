name=input()
main_salary=float(input())
sold_money=float(input())
bonus_money=(sold_money*15)/100
full_salary=main_salary+bonus_money
updated_full_salary = "{:.2f}".format(full_salary)
print("TOTAL = R$",updated_full_salary)