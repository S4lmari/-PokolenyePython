# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summ = 0
# for num in numbers:
#     summ += num ** 2
# print(summ)
n = int(input())
list = []

for i in range(n):
    list.append(int(input()))
for el in list:
    print(el)
print('')
for j in list:
    x = j ** 2 + 2 * j + 1
    print(x)
