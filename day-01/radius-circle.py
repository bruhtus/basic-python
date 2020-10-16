radius_input = input('Circle radius: ')
radius = float(radius_input) #in case you want to input float number, who knows
phi = (22/7)

area_of_circle = phi*(radius**2)
circum_of_circle = 2*phi*radius

print(f'area of a circle: {area_of_circle}')
print(f'circumference of a circle: {circum_of_circle}')
