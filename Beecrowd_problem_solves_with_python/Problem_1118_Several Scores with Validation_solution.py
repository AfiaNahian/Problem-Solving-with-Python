while(1):
    c = 0
    r = 0
    while(c<2):
        a = float(input())
        if(a < 0 or a >10):
            print("nota invalida")
            continue
        else:
            r += a
            c += 1
        if (c == 2):
            r = r / 2
            r = "{:.2f}".format(r)
            print(f"media = {r}")
            break

    while(1):
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if(x == 1 or x == 2):
            break
    if(x == 2):
        break