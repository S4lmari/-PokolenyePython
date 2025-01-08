# x = int(input())
#
# if -1 < x < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# x = int(input())
#
# if x <= -3 or x >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
#
# if -30 < x <= -2 or 7 < x <= 25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")


# x = int(input())
#
# if 1000 <= x <= 9999 and ((x % 17) == 0 or (x % 7) == 0):
#     print("YES")
# else:
#     print("NO")

# a+b>c
# a+c>b
# b+c>a
# a,b,c = int(input()),int(input()),int(input())
# ab = a+b
# ac = a+c
# bc = b+c
# if ab>c and ac>b and bc>a:
#     print("YES")
# else:
#     print("NO")


# h = int(input())
#
# if (h % 4 == 0 and h % 100 != 0) or (h % 400 == 0):
#     print('YES')
# else:
#     print('NO')


# x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())
#
# if x_1 == x_2 or y_1 == y_2:
#     print('YES')
# else:
#     print('NO')


x_1, y_1, x_2, y_2 = int(input()), int(input()), int(input()), int(input())

if ((-1<= (x_1 - x_2) <= 1) and (-1<= (y_1 - y_2) <= 1)):
    print('YES')
else:
    print('NO')
