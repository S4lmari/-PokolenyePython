# n = int(input()) #1
# s = 0
# while n > 1:
#     if n % 2 == 0: #2
#         s += (n % 10) #3
#     n //= 10
# if s == 0:
#     print(0)
# else:
#     print(s)
from pickle import PROTO

# n = 8  # 1
# count = 0
# maximum = 10 ** 12
# maxi = -10**12
#
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x < maximum and x > maxi:
#             maxi = x
# if count > 0:
#     print(count)
#     print(maxi)
# else:
#     print('NO')


# n = 4
# count = 0
# maximum = 10**8 #1
# maxi = -10**8
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x < maximum and x > maxi:
#             maxi = x
#
# if count > 0:
#     print(count)
#     print(maxi)
# else:
#     print('NO')


# n = int(input())
#
# if 3<= n <=19:
#     print("*"*19)
#     for i in range(1,n-1):
#         print("*","*",sep=(" "*17))
#     print("*"*19)


# n = int(input())
#
# if n > 99:
#     while n >= 1000:
#         n = n // 10
# last = n % 10
# print(last)


# n = int(input())
#
# countthree = 0
# countlast = 0
# countnumbered = 0
# sumabovefive = 0
# multipyaboveseven = 1
# countbetweenzerotofive = 0
#
# x = n
# lastnum = n % 10
# while x > 1:
#     last = x % 10
#
#     if last == 3:
#         countthree += 1
#     if last == lastnum:
#         countlast += 1
#     if last % 2 == 0:
#         countnumbered += 1
#     if last > 5:
#         sumabovefive += last
#     if last >7:
#         multipyaboveseven *= last
#     if last == 0 or last == 5:
#         countbetweenzerotofive += 1
#     x //= 10
#
# print(countthree)
# print(countlast)
# print(countnumbered)
# print(sumabovefive)
# print(multipyaboveseven)
# print(countbetweenzerotofive)


for a in range(1, 33):
    for c in range(1, a):
        for d in range(1, c):
            for b in range(1, d):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a**3 + b**3)