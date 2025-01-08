# parol = input()
# parol_2 = input()
#
#
# if parol == parol_2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# a = int(input())
#
# div, mod = divmod(a, 2)
# if mod > 0:
#    print("Нечетное")
# else:
#     print("Четное")
#
# s = int(input())
# t = n // 1000
# s = (n % 1000) // 100
# d = (n % 100) // 10
# e = n % 10
#
# if t + e == s - d:
#     print('ДА')
# else:
#     print("НЕТ")

# age = int(input())
#
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# a, b, c = int(input()), int(input()), int(input())
#
# if b-a == c-b:
#     print('YES')
# else:
#     print("NO")

# a, b = int(input()), int(input())
#
# if a < b:
#     print(a)
# else:
#     print(b)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# if a < b:
#     ab = a
# else:
#     ab = b
#
# if c < d:
#     cd = c
# else:
#     cd = d
#
# if ab < cd:
#     print(ab)
# else:
#     print(cd)

# age = int(input())
#
# if age <= 13:
#     print("детство")
# elif 14 <= age <= 24:
#     print("молодость")
# elif 25 <= age <= 59:
#     print('зрелость')
# else:
#     print("старость")

a, b, c = int(input()), int(input()), int(input())

if a > 0 and b > 0 and c > 0:
    print(a + b + c)
elif a > 0 and b > 0 and c < 0:
    print(a + b)
elif a > 0 and b < 0 and c > 0:
    print(a + c)
elif a > 0 and b < 0 and c < 0:
    print(a)
elif a < 0 and b > 0 and c > 0:
    print(b + c)
elif a < 0 and b > 0 and c < 0:
    print(b)
elif a < 0 and b < 0 and c > 0:
    print(c)
else:
    print(0)
