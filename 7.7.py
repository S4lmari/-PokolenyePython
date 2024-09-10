# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# mx = -10**6
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx:
#             mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print("NO")

# s = 0 #1
# for i in range(1, 8): #2
#     n = int(input()) #3
#     if n % 2 == 0:
#         s += n
# if s != 0: #4
#     print(s)
# else:
#     print(0)

# n = int(input())
# max_digit = -10**6 #5
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0 or digit == 0: #2
#         if digit > max_digit: #3
#             max_digit = digit #4
#     n //= 10 #1
# if max_digit > -10**6:
#     print(max_digit)
# else:
#     print('NO')

# n = int(input())
# while n >= 10: #2
#     n //= 10 #1
# print(n)

n = int(input()) #1
product = 1 #2
while n > 0: #3
    digit = n % 10
    product = product * digit
    n //= 10
print(product)