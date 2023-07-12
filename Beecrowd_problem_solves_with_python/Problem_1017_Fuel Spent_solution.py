hour = int(input())
speed = int(input())

distance_travelled = hour * speed
fuel_needed = distance_travelled / 12
precised_fuel_needed = "{:.3f}".format(fuel_needed)
print(precised_fuel_needed)