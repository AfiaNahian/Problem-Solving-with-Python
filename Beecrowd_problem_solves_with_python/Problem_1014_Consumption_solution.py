km = int(input())
fuel = float(input())

km_per_fuel = km/fuel
precised_km_per_fuel = "{:.3f}".format(km_per_fuel)
print(precised_km_per_fuel,"km/l")