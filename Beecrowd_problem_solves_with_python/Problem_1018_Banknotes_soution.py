a = int(input())
x = a//100
y = (a%100)//50
z = ((a%100)%50)//20
p = (((a%100)%50)%20)//10
q = ((((a%100)%50)%20)%10)//5
m = (((((a%100)%50)%20)%10)%5)//2
n = (((((a%100)%50)%20)%10)%5)%2

print(a)
print(x,"nota(s) de R$ 100,00")
print(y,"nota(s) de R$ 50,00")
print(z,"nota(s) de R$ 20,00")
print(p,"nota(s) de R$ 10,00")
print(q,"nota(s) de R$ 5,00")
print(m,"nota(s) de R$ 2,00")
print(n,"nota(s) de R$ 1,00")