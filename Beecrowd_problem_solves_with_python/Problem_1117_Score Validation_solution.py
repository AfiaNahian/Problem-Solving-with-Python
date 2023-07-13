c = 0
r = 0
while(1):
    a = float(input())
    if(a < 0 or a >10):
        print("nota invalida")
        continue
    else:
        r += a
        c += 1
    if(c == 2):
        r = r/2
        r = "{:.2f}".format(r)
        print(f"media = {r}")
        break
