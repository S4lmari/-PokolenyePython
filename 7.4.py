# text = " "
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()


# text = ''
# count = 0
#
# while text != 'стоп' and text != 'достаточно' and text != 'хватит':
#     text = input()
#     if text != 'стоп' and text != 'достаточно' and text != 'хватит':
#         count += 1
# print(count)

# num = int(input())
#
# while num % 7 == 0:
#     print(num)
#     num = int(input())

# num = int(input())
# sum = 0
# while num >= 0:
#     sum += num
#     num = int(input())
# print(sum)

num = int(input())
sum = 0
while 1 <= num <= 5:
    if num == 5:
        sum += 1
    num = int(input())
print(sum)