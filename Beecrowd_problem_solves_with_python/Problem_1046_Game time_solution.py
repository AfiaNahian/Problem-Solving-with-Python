hour = input().split(' ')
s,e = hour
s=int(s)
e=int(e)

if(s==e):
    print("O JOGO DUROU 24 HORA(S)")
elif(s>e):
    duration=24-s+e
    print("O JOGO DUROU {} HORA(S)".format(duration))
else:
    duration=e-s
    print("O JOGO DUROU {} HORA(S)".format(duration))