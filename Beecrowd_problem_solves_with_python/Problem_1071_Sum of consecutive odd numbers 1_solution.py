a1 = int(input())
a2 = int(input())
total = 0
if (a2 < a1):
    temp = a1
    a1 = a2
    a2 = temp

for i in range(a1 + 1, a2):
    if (i % 2 == 1 or i % 2 == -1):
        total += i

print(total)