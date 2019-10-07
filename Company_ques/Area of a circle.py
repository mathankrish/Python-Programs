# Area of a circle

import math

radius = int(input("Enter the radius of a circle: "))

area_of_a_circle = round(math.pi * (radius**2), 2)

print("The area of the circle of radius {0} is {1}".format(radius, area_of_a_circle))