# flag = None
# list = []
# while flag == None:
#     st = input()
#     if st != "КОНЕЦ":
#         list.append(st)
#     else:
#         flag = True
#     st = ""
# print(f'Минимальная строка ⬇️: {min(list)}')
# print(f'Максимальная строка ⬆️: {max(list)}')

# list = []
# for i in range(4):
#     list.append(input())
# max_st = max(list)
# min_st = min(list)
# magic = (ord(max_st[-1])*ord(min_st[-1]))**2
#
# print(magic)

# n = int(input())
# list = []
# for i in range(n):
#     class_number = input()
#     list.append(class_number)
#
# for j in list:
#     if len(j) == 2:
#         if j[0] in "0123456789" and 1040 <= ord(j[1]) <= 1055 and len(j) == 2:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")

# st1, st2 = input(), input()
#
# lower1 = st1.lower()
# lower2 = st2.lower()
# new1 = ""
# new2 = ""
# for i in lower1:
#     if i.isalpha():
#         new1 += i
# for j in lower2:
#     if j.isalpha():
#         new2 += j
#
# if len(new1) == len(new2) and new1 == new2:
#     print("YES")
# else:
#     print("NO")

# list = []
# for i in range(3):
#     list.append(input())
#
# max_st = max(list)
# min_st = min(list)
# list.remove(max_st)
# list.remove(min_st)
# print(min_st,list[0],max_st)

# n = input()
# print(n.find("."),n.find("«")) # 8 and 13
# print(n[:n.find(".")-1]+n[n.find("«")+1:-1])

# ---СОРТИРОВЩИК КНИГ---
n = int(input())
list = []
for i in range(n):
    book = input()
    name_book = book[:book.find(".")-1]+book[book.find("«")+1:-1]
    list.append(name_book)

if list == sorted(list):
    print("YES")
else:
    print("NO")

