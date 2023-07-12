input_value = input().split(' ')
a, b, c, d = input_value
a = float(a)
b = float(b)
c = float(c)
d = float(d)

f = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10
p_f = "{:.1f}".format(f)
print("Media: {}".format(p_f))
if (f >= 7.0):
    print("Aluno aprovado.")

if ((f >= 5.0) and (f < 7.0)):
    print("Aluno em exame.")
    e = float(input())
    g = (f + e) / 2.0
    if (g >= 5.0):
        print("Nota do exame: {}\nAluno aprovado.\nMedia final: {}".format(e, g))
    if (g < 5.0):
        print("Nota do exame: {}\nAluno reprovado.\nMedia final: {}".format(e, g))

if (f < 5.0):
    print("Aluno reprovado.")