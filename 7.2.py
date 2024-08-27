# m,n = int(input()),int(input())
#
# for i in range(m,n):
#     print(i)
# print(n)

m, n = int(input()), int(input())

if m >= n:
    for i in range(m, n, -1):
        print(i)
    print(n)
else:
    for i in range(m, n):
        print(i)
    print(n)
