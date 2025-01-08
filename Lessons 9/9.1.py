# s = 'abcdef'
# for c in s:
#     print(c)
from itertools import count

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# for i in s:
#     if i == "w":
#         print(i)

# n = input()
#
# for i in range(0,len(n),2):
#     print(n[i])
#
# n = input()
#
# for i in range(len(n)-1,-1,-1):
#     print(n[i])
# n = input()
# s = input()
# f = input()
#
# print(s[0],n[0],f[0],sep='')
#
# n = input()
# summ = 0
# for i in n:
#     summ += int(i)
# print(summ)
# # n = input()
# # count = 0
# # for i in n:
# #     for x in range(10):
# #         if i == str(x):
# #             count +=1
# # if count > 0:
# #     print('Цифра')
# # else:
# #     print("Цифр нет")
# n = input()
# countp = 0
# countm = 0
#
# for i in n:
#     if i == "+":
#         countp +=1
#     if i == "*":
#         countm += 1
# print("Символ + встречается" ,countp, "раз")
# print("Символ + встречается" ,countm, "раз")

# n = input()
# count = 0
# for i in range(1,len(n)):
#     if n[i] == n[i-1]:
#         count +=1
# print(count)

# n = input()
#
# countglas = 0
# countsogl = 0
#
# for i in n:
#     if i in "ауоыиэяюе" or i in "АУОЫИЭЯЮЕ":
#         countglas += 1
#     elif i in "бвгджзйклмнпрстфхцчшщ" or i in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
#         countsogl += 1
# print("Количество гласных букв равно", countglas)
# print("Количество согласных букв равно", countsogl)

n = int(input())

print(format(n,'b'))
