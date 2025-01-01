# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summ = 0
# for num in numbers:
#     summ += num ** 2
# print(summ)
# n = int(input())
# list = []
#
# for i in range(n):
#     list.append(int(input()))
# for el in list:
#     print(el)
# print('')
# for j in list:
#     x = j ** 2 + 2 * j + 1
#     print(x)
# n = int(input())
# list = []
# for el in range(n):
#     list.append(int(input()))
#
# list.remove(max(list))
# list.remove(min(list))
#
# for j in list:
#     print(j)
from itertools import count

# n = int(input())
# list = []
# for i in range(n):
#     st = input()
#     if st in list:
#         continue
#     else:
#         list.append(st)
#
# for j in list:
#     print(j)
# n = int(input())
# list = []
# for i in range(n):
#     list.append(input())
# promt = input()
# for el in list:
#     if promt.lower() in el.lower():
#         print(el)
n = int(input())
list = []

for i in range(n):
    list.append(input())

k = int(input())
list_request = []

for j in range(k):
    list_request.append(input())

for el in list:
    count = 0
    for r in list_request:
        if r.lower() in el.lower():
            count += 1
        if count == k:
            print(el)
