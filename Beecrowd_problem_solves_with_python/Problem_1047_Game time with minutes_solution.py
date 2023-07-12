input_value = input().split(' ')
a, b, c, d = input_value
a = int(a)
b = int(b)
c = int(c)
d = int(d)

dif = ((c * 60) + d) - ((a * 60) + b)
if (dif <= 0):
    dif += 24 * 60

hour = dif // 60
minute = dif % 60
print(f"O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)")