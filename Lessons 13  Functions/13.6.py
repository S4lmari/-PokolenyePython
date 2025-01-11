import math


# def get_middle_point(x1, y1, x2, y2):
#     middle_x = (x1+x2)/2
#     middle_y = (y1+y2)/2
#     return middle_x,middle_y
#
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
#
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# def get_circle(radius):
#     C = 2 * math.pi * radius
#     S = math.pi * (radius ** 2)
#     return C,S
#
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)

# ---Корни уравнения---
def solve(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        x1 = ((-b - d ** 0.5) / (2 * a))
        x2 = ((-b + d ** 0.5) / (2 * a))
        return min(x1, x2), max(x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        return  x
    else:
        return 'Нет корней'

a, b, c = float(input()), float(input()), float(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
