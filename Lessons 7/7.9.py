from math import factorial

from unicodedata import numeric

# n = int(input())
# number = 0
#
# for i in range(1,n+1):
#     print(end='\n')
#     for j in range(1,i+1):
#         number += 1
#         print(number,end=' ')
# 3

# 1
# 121
# 12321

# n = int(input())
#
#
# for i in range(1,n+1):
#     print(end='\n')
#     for j in range(1,i+1):
#         print(j,end='')
#     if j == i and j != 1:
#         for k in range(j-1,0,-1):
#             print(k,end='')


# a = int(input())
# b = int(input())
#
# maxsum = 0
# maxnumber = 0
#
# for i in range(a,b+1):
#     sum = 0
#
#     for j in range(1,i+1):
#         if i % j == 0:
#             sum += j
#
#     if sum >= maxsum:
#         maxsum = sum
#         maxnumber = i
#
# print(maxnumber,maxsum)

# n = int(input())
# count = 0
#
# for i in range(1, n + 1):
#     count = 0
#     for x in range(1, i + 1):
#         if i % x == 0:
#             count += 1
#     print(i, + count * '+', sep=(''))

# n = int(input())
# last = 0
#
# while n > 9:
#     summ = 0
#     while n > 0:
#         last = n % 10
#         summ += last
#         n //= 10
#     n = summ
# print(n)

# import math
# n = int(input())
# total = 0
#
# for i in range(1, n + 1):
#
#     for x in range(1, i + 1):
#         f = factorial(x)
#     total += f
#
# print(total)

a = int(input())
b = int(input())

for i in range(a, b + 1):

    count = 0

    for x in range(1, i + 1):
        if i % x == 0:
            count += 1
    if count == 2:
        print(i)



