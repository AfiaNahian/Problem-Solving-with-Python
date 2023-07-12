s = float(input())
if (s >= 0 and s <= 400):
    r = s * 0.15
    total = s + r
    p_r = "{:.2f}".format(r)
    p_total = "{:.2f}".format(total)
    print("Novo salario: {}".format(p_total))
    print("Reajuste ganho: {}".format(p_r))
    print("Em percentual: 15 %")

if (s > 400.00 and s <= 800.00):
    r = s * 0.12
    total = s + r
    p_r = "{:.2f}".format(r)
    p_total = "{:.2f}".format(total)
    print("Novo salario: {}".format(p_total))
    print("Reajuste ganho: {}".format(p_r))
    print("Em percentual: 12 %")

if (s > 800.00 and s <= 1200.00):
    r = s * 0.10
    total = s + r
    p_r = "{:.2f}".format(r)
    p_total = "{:.2f}".format(total)
    print("Novo salario: {}".format(p_total))
    print("Reajuste ganho: {}".format(p_r))
    print("Em percentual: 10 %")

if (s > 1200.00 and s <= 2000.00):
    r = s * 0.07
    total = s + r
    p_r = "{:.2f}".format(r)
    p_total = "{:.2f}".format(total)
    print("Novo salario: {}".format(p_total))
    print("Reajuste ganho: {}".format(p_r))
    print("Em percentual: 7 %")

if (s > 2000):
    r = s * 0.04
    total = s + r
    p_r = "{:.2f}".format(r)
    p_total = "{:.2f}".format(total)
    print("Novo salario: {}".format(p_total))
    print("Reajuste ganho: {}".format(p_r))
    print("Em percentual: 4 %")