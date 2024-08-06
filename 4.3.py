# n = int(input())
# k = int(input())
#
# if n>k:
#     print('NO')
# elif n<k:
#     print('YES')
# else:
#     print("Don't know")

# a,b,c = int(input()),int(input()),int(input())
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a==c or b==c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# a, b, c = int(input()), int(input()), int(input())
#
# if a > b and a > c:
#     if b > c:
#         print(b)
#     else:
#         print(c)
# elif b > a and b > c:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > a:
#         print(b)
#     else:
#         print(a)

# x = int(input())
#
# if x in [1, 3, 5, 7, 8, 10, 12]:
#     print(31)
# elif x in [4, 6, 9, 11]:
#     print(30)
# else:
#     print(28)

# w = int(input())
#
# if w <60:
#     print("Легкий вес")
# elif 60 <= w <64:
#     print("Первый полусредний вес")
# elif 64 <= w < 69:
#     print("Полусредний вес")

# x,y,s = int(input()),int(input()),str(input())
#
# if s == "+":
#     print(x+y)
# elif s == "-":
#     print(x-y)
# elif s == "*":
#     print(x*y)
# elif s == '/':
#     if y == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(x/y)
# else:
#     print('Неверная операция')


# x, y = str(input()), str(input())
#
# if x == "красный":
#     if y == "красный":
#         print('красный')
#     elif y == "синий":
#         print("фиолетовый")
#     elif y == "желтый":
#         print("оранжевый")
#     elif y != ("красный", "синий", "желтый"):
#         print("ошибка цвета")
# elif x == "синий":
#     if y == "красный":
#         print("фиолетовый")
#     elif y == "синий":
#         print("синий")
#     elif y == "желтый":
#         print("зеленый")
#     elif y != ("красный", "синий", "желтый"):
#         print("ошибка цвета")
# elif x == "желтый":
#     if y == "красный":
#         print("оранжевый")
#     elif y == "синий":
#         print("зеленый")
#     elif y == "желтый":
#         print("желтый")
#     elif y != ("красный", "синий", "желтый"):
#         print("ошибка цвета")
# elif x != ("красный", "синий", "желтый"):
#     print("ошибка цвета")

# x = int(input())
#
# if x == 0:
#     print('зеленый')
# elif 1 <= x <= 10 or 19 <= x <= 28:
#     if x % 2 != 0:
#         print('красный')
#     else:
#         print('черный')
# elif 11 <= x <= 18 or 28 <= x <= 36:
#     if x % 2 != 0:
#         print('черный')
#     else:
#         print('красный')
# else:
#     print('ошибка ввода')

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if c > b or a > d:
    print("пустое множество")

elif b == c or d == a:
    if b == c:
        print(c)
    else:
        print(d)

elif a <= c < b < d:
    print(c, b)
elif c <= a < d < b:
    print(a, d)

elif a < c < d <= b:
    print(c, d)
elif c < a < b <= d:
    print(a, b)

elif a==c and b==d:
    print(a,b)