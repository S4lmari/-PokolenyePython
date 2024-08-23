# a = float(input())
# b = float(input())
#
# print(a*b*0.5)

# s = float(input())
# a = float(input())
# b = float(input())
#
#
# vs = a+b
# t = s/vs
# print(t)

# x = float(input())
#
# if x != 0:
#     print(x**-1)
# else:
#     print("Обратного числа не существует")

# x = float(input())
#
# print((5/9)*(x-32))

# x = float(input())
#
# if x > 2:
#     print(2*10.5+(x-2)*4)
# else:
#     print(x*10.5)

# x = float(input())
#
# y = int(x)
# f = ((x-y)*10)
# ff= int(f)
#
# print(ff)

# x = float(input())
# y = int(x)
# d = x-y
# print(d)

# num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
# print(num)

# a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
#
# numax = max(a,b,c,d,e)
# numin = min(a,b,c,d,e)
#
# print("Наименьшее число =", numin)
# print("Наибольшее число =", numax)

# a, b, c = int(input()), int(input()), int(input())
# numax = max(a, b, c)
# numin = min(a, b, c)
#
# sum = a + b + c
# sred = sum - numin - numax
#
# print(numax, sred, numin, sep=("\n"))

# x = int(input())
#
# s = x // 100
# d = (x // 10) % 10
# e = x % 10
#
# numax = max(s,d,e)
# numin = min(s,d,e)
# sum = s+d+e
# sred = sum - numin - numax
#
# if numax-numin==sred:
#     print("Число интересное")
# else:
#     print("Число неинтересное")

# a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
#
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())

print(abs(x1-x2)+abs(y1-y2))