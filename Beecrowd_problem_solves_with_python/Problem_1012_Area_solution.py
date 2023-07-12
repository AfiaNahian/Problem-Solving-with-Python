abc_values = input().split(" ")
a,b,c = abc_values

a = float(a)
b = float(b)
c = float(c)

triangle = (1/2.0)*a*c
circle = 3.14159*c*c
trapizium = (1/2.0)*(a+b)*c
square = b*b
rectangle = a*b

p_triangle = "{:.3f}".format(triangle)
p_circle = "{:.3f}".format(circle)
p_trapizium = "{:.3f}".format(trapizium)
p_square = "{:.3f}".format(square)
p_rectangle = "{:.3f}".format(rectangle)

print("TRIANGULO:",p_triangle)
print("CIRCULO:",p_circle)
print("TRAPEZIO:",p_trapizium)
print("QUADRADO:",p_square)
print("RETANGULO:",p_rectangle)