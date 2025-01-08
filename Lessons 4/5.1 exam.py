# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».
# x = int(input())
#
# if (x % 100) == 0:
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if ((x1 + y1) % 2) == 0 and ((x2 + y2) % 2) == 0:
#     print("YES")
# elif ((x1 + y1) % 2) != 0 and ((x2 + y2)) % 2 != 0:
#     print("YES")
# else:
#     print("NO")


# x = int(input())
# g = str(input())
#
# if 10 <= x <= 15 and g == "f":
#     print("YES")
# else:
#     print("NO")


# x = int(input())
#
# if 1 <= x <= 3:
#     print(x * "I")
# elif 4 <= x <= 8:
#     if x == 4:
#         print("IV")
#     else:
#         print("V" + (x - 5) * "I")
# elif x == 9:
#     print("IX")
# elif x == 10:
#     print("X")
# else:
#     print("Ошибка")

# x = int(input())
#
# if x % 2 != 0 or (x % 2 == 0 and 6 <= x <= 20):
#     print("YES")
# elif (x % 2 == 0 and 2 <= x <= 5) or (x % 2 == 0 and 20 < x):
#     print("NO")

# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if x1 != x2 and y1 != y2:
#     if ((x1 + y1) % 2) == 0:
#         k1 = "w"
#     elif ((x1 + y1) % 2) != 0:
#         k1 = "b"
#     if ((x2 + y2) % 2) == 0:
#         k2 = "w"
#     elif ((x2 + y2) % 2) != 0:
#         k2 = "b"
#     if k1 == k2:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")


# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if (x1 - x2)**2 == 1 and (y1 - y2)**2 == 4:
#     print("YES")
# elif (x1 - x2)**2 == 4 and (y1 - y2)**2 == 1:
#     print("YES")
# else:
#     print("NO")


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2)) or (x1 == x2 or y1 == y2):
    print('YES')
else:
    print('NO')


