input_value = input().split(' ')
a,b,c= input_value
a=int(a)
b=int(b)
c=int(c)

list_3num = []
list_3num.append(a)
list_3num.append(b)
list_3num.append(c)

list_3num.sort(key=None, reverse=False)
for i in list_3num:
    print(i)
print('')
print(a)
print(b)
print(c)