while (1):
    point = input().split(" ")
    x,y=point
    x=int(x)
    y=int(y)
    if(x==0 or y==0):
        break
    elif (x > 0 and y > 0):
        print("primeiro")
    elif (x > 0 and y < 0):
        print("quarto")
    elif (x < 0 and y < 0):
        print("terceiro")
    else:
        print("segundo")