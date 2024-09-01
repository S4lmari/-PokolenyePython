# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# a, b = int(input()), int(input())
#
# cube = 0
#
# for i in range(a, b+1):
#     if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#         cube += 1
# print(cube)


# n = int(input())
# sum = 0
#
# for _ in range(n):
#     x = int(input())
#     sum += x
#
# print(sum)

# import math
#
# n = int(input())
# x = 0
# for i in range(1,n+1):
#     x += (1/i)
#     expression = x - math.log(n)
#
# print(expression)


# n = int(input())
# summ = 0
# for i in range(1,n+1):
#     if (i**2 % 10) == 2 or (i**2 % 10) == 5 or (i**2 % 10) == 8:
#         summ += i
#
# print(summ)

# n = int(input())
# x = 1
#
# for i in range(1,n+1):
#     x *= i
# print(x)

# summ = 1
# for i in range(10):
#     x = int(input())
#     if x != 0:
#         summ *= x
# print(summ)

# n = int(input())
# summ = 0
# for i in range(1,n+1):
#     if (n%i) == 0:
#         summ += i
# print(summ)

# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += ((-1) ** (i + 1)) * i
# print(summ)

n = int(input())
largest  = 0
largest_2 = 0

for i in range(n):
    x = int(input())

    if x > largest:
        largest = x

    if x < largest and x > largest_2:
        largest_2 = x


print(largest, largest_2, sep="\n")
