#2. Center Point 

#You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. 
#Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
#If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.

from math import floor


def closer_coordinates(param_one, param_two):
    if param_one <= param_two:
        return f'({x1}, {x2})'
    elif param_two <= param_one:
        return f'({y1}, {y2})'


x1 = floor(float(input()))
x2 = floor(float(input()))
y1 = floor(float(input()))
y2 = floor(float(input()))
sum_x = abs(x1) + abs(x2)
sum_y = abs(y1) + abs(y2)
print(closer_coordinates(sum_x, sum_y))
