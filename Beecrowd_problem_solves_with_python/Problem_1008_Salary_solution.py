num=int(input())
hour=int(input())
money_per_hour=float(input())
salary=hour * money_per_hour
updated_salary = "{:.2f}".format(salary)
print("NUMBER =",num)
print("SALARY = U$",updated_salary)