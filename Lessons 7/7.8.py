# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
#
# for _ in range(n):
#     for _ in range(3):
#         print(n, end=(" "))
#     print()

# n = int(input())
#
# for i in range(1,n+1):
#     print("")
#     for j in range(1,10):
#         summ = i + j
#         print(i,'+',j,'=',summ)

# n = int(input())
# middle =  n//2
#
# for i in range(1,middle+1):
#     print(i*"*")
#
#
# for i in range(middle+1,0,-1):
#     print(i*"*")

# n =int(input())
#
# for i in range(1,n+1):
#     print(str(i)*i)

# total = 0
# for b in range(1, 10):
#     for k in range(1, 20):
#         for t in range(1, 200):
#             if 10*b + 5*k + 0.5*t == 100 and b+k+t == 100:
#                 total += 1
#                 print('b =', b, 'k =', k, 't =', t)
# print('Общее количество натуральных решений =', total)

for e in range(151):
    print(e)
    for a in range(1, e):
        for b in range(a, e):
            for c in range(b, e):
                for d in range(c, e):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        summ = a + b + c + d + e
                        print(a, b, c, d, e, summ)

