import math
point_a = input().split(' ')
point_b = input().split(' ')
x1,y1=point_a
x2,y2=point_b

x1=float(x1)
x2=float(x2)
y1=float(y1)
y2=float(y2)
distance= math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
precised_distance="{:.4f}".format(distance)
print(precised_distance)