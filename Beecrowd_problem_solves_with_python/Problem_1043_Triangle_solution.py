line_input = input().split(' ')
a,b,c= line_input
a=float(a)
b=float(b)
c=float(c)
if((a+b>c) and (b+c>a) and (c+a>b)):
    p="{:.1f}".format(a+b+c)
    print("Perimetro =",(p))
else:
    d=(1/2.0)*(a+b)*c
    p_d="{:.1f}".format(d)
    print("Area =",p_d)