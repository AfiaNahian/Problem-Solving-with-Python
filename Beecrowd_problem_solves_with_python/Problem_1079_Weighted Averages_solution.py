t = int(input())
for i in range (1,t+1):
    input_value = input().split(' ')
    a, b, c = input_value
    a = float(a)
    b = float(b)
    c = float(c)
    r = (a*2+b*3+c*5)/10
    r = "{:.1f}".format(r)
    print(f"{r}")