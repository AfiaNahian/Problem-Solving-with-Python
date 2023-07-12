earning = float(input())
if (earning >= 0.00 and earning <= 2000.00):
    print("Isento")

if (earning > 2000.00 and earning <= 3000.00):
    taxed_money = earning - 2000.00
    tax = taxed_money * 0.08
    p_tax = "{:.2f}".format(tax)
    print("R$ {}".format(p_tax))

if (earning > 3000.00 and earning <= 4500.00):
    taxed_money = earning - 3000.00
    tax = 80 + taxed_money * 0.18
    p_tax = "{:.2f}".format(tax)
    print("R$ {}".format(p_tax))

if (earning > 4500.00):
    taxed_money = earning - 4500.00
    tax = 350 + taxed_money * 0.28
    p_tax = "{:.2f}".format(tax)
    print("R$ {}".format(p_tax))