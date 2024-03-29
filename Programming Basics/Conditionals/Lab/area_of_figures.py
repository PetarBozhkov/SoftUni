#7. Лица на фигури
#Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й. Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
#· Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
#· Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
#· Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
#· Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
#Резултатът да се закръгли до 3 цифри след десетичната запетая.

import math
figure = input()
side_a = float(input())
area = 0

if figure == "square":
    area = side_a * side_a
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    area = math.pi * side_a * side_a
    print(f"{area:.3f}")
elif figure == "triangle":
    h = float(input())
    area = (side_a * h) / 2
    print(f"{area:.3f}")
