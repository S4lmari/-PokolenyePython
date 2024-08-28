# m,n = int(input()),int(input())
#
# for i in range(m,n):
#     print(i)
# print(n)

# m, n = int(input()), int(input())
#
# if m >= n:
#     for i in range(m, n, -1):
#         print(i)
#     print(n)
# else:
#     for i in range(m, n):
#         print(i)
#     print(n)

# m, n = int(input()), int(input())
#
# if (m-n)> 1:
#     for i in range(m, n, -1):
#         if i % 2 != 0:
#             print(i)
#     if n % 2 != 0:
#         print(n)
#
# elif abs(m - n) == 1:
#     if m % 2 != 0:
#         print(m)
#     else:
#         print(n)


# m, n = int(input()), int(input())
#
#
# for i in range(m, n):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)
#
# if n % 17 == 0 or n % 10 == 9 or (n % 3 == 0 and n % 5 == 0):
#     print(n)


n = int(input())

for i in range(10):
    print(n,'x', i+1, '=',n*(i+1))