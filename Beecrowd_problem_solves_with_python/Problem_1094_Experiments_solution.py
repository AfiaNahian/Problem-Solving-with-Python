t= int(input())
total=0
co = 0
ra = 0
sa = 0
for i in range (1,t+1):
    num_animal=input().split(" ")
    n,c = num_animal
    n = int(n)
    c = str(c)
    total += n
    if(c=='C'):
        co += n
    elif (c == 'R'):
        ra += n
    else:
        sa += n

p_co = (co/total)*100
p_ra = (ra/total)*100
p_sa = (sa/total)*100

p_co = "{:.2f}".format(p_co)
p_ra = "{:.2f}".format(p_ra)
p_sa = "{:.2f}".format(p_sa)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {co}\nTotal de ratos: {ra}\nTotal de sapos: {sa}")
print(f"Percentual de coelhos: {p_co} %\nPercentual de ratos: {p_ra} %\nPercentual de sapos: {p_sa} %")


