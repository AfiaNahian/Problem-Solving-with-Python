num = int(input())
c_in = 0
c_out = 0
for i in range(1, num + 1):
    a = int(input())
    if (a >= 10 and a <= 20):
        c_in += 1
    else:
        c_out += 1

print("{} in".format(c_in))
print("{} out".format(c_out))