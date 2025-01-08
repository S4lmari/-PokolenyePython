# for i in range(10):
#
#     print("Python is awesome!")


# text = input()
# n = int(input())
# for i in range(n):
#
#     print(text)

# for i in range(6):
#     print('A'*3)
#
# for i in range(5):
#     print('B'*4)
# print("E")
# for i in range(9):
#     print('T'*5)
# print('G')


# n = int(input())
#
# for i in range(n):
#
#     print('*'*19)

# n = input()
#
# for i in range(10):
#
#     print(i, n)

# n = int(input())
#
# for i in range(n,0,-1):
#     print(i*'*')

m, p, n = int(input()), int(input()), int(input())

print('1', m)
for i in range(n-1):
    quantity = m * (1 + p / 100)
    print(i + 2, quantity)

    m = quantity
