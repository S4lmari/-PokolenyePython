# x = input()
# lastchr = "Я"
# if x != lastchr:
#     next = ord(x)+1
#     print(chr(next))
# else:
#     print("Дальше букв нет")
from itertools import count
from pickle import UNICODE

# a,b= int(input()),int(input())
#
# for i in range(a,b+1):
#     print(chr(i),end=" ")

# s = input()
#
# for i in s:
#     print(ord(i),end=" ")

# max = 0
# maxword = None
# for i in range(4):
#     s = input()
#     summ = 0
#     for j in s:
#         summ += ord(j)
#         if summ > max:
#             max = summ
#             maxword = s
# print(maxword)

# s = input()
# summ = 0
# for i in s:
#     summ += ord(i)*3
#
#
# print(f"Текст сообщения: '{s}'")
# print(f"Стоимость сообщения: {summ}🐝")

# ---ЗАМЕНА БУКВ ENG на RU---
# s = input()
# ru = "еуорахсЕТОРАНХСВМ"
# eng = "eyopaxcETOPAHXCBM"
# newtext = ""
#
# for i in s:
#     if eng.find(i) >=0:
#         newtext += ru[eng.find(i)]
#     else:
#         newtext += i
#
# summ = 0
# for i in s:
#     summ += ord(i)*3
#
# print(f"Старая стоимость: {summ}🐝")
#
# summ = 0
# for i in newtext:
#     summ += ord(i)*3
# print(f"Новая стоимость: {summ}🐝")

# ---ДЕКОДЕР ШИФРА ЦЕЗАРЯ---
# n = int(input())
# s = input()
# newtext = ""
# for i in s:
#     if (ord(i) - n) < 97:
#         newtext += chr(ord(i) - n + 26)
#     else:
#         newtext += chr(ord(i) - n)
# print(newtext)

# ===CБОЙ СИСТЕМЫ---
s = input()

for i in range(1040, 1104):
    unicode_code = f"[u-{i}]"
    if unicode_code in s:
        s = s.replace(unicode_code, chr(i))

print(s)
