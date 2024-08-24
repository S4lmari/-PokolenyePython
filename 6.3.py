from math import *

# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
#
# p = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
# print(p)

# r = float(input())
#
# S = math.pi * math.pow(r, 2)
# C = 2 * math.pi * r
#
# print(S, C, sep=('\n'))

# a,b = float(input()), float(input())
#
# arifm = (a+b)/2
# geom = sqrt(a*b)
# garmon = (2*a*b)/(a+b)
# kvadrat = sqrt(((pow(a,2)+pow(b,2))/2))
#
# print(arifm,geom,garmon,kvadrat,sep=('\n'))

# x = float(input())
# xr = radians(x)
#
# print(sin(xr)+cos(xr)+pow(tan(xr),2))

# x = float(input())
#
# print(ceil(x)+floor(x))

# a, b, c = float(input()), float(input()), float(input())
#
# d = (b ** 2) - (4*a*c)
#
#
# if d > 0:
#     x1 = ((-b - sqrt(d)) / (2 * a))
#     x2 = ((-b + sqrt(d)) / (2 * a))
#     print(min(x1,x2),max(x1,x2),sep=('\n'))
# elif d == 0:
#     x = -b/(2*a)
#     print(x)
# else:
#     print('Нет корней')

n,a = int(input()), float(input())

# angle = radians(pi/n)
s = (n*(a**2))/(4*(tan(pi/n)))
print(s)