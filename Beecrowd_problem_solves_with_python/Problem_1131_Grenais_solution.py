inter = 0
gremio =0
draw = 0
game = 0
while (1):
    game +=1
    goals = input().split(' ')
    a,b=goals
    a=int(a)
    b=int(b)
    print("Novo grenal (1-sim 2-nao)")
    if (a > b):
        inter += 1
    elif (a < b):
        gremio += 1
    else:
        draw += 1
    c = int(input())
    if(c == 1):
        continue
    else:
        break

print(f"{game} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{draw}\nInter venceu mais")