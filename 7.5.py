# num = int(input())
#
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num //= 10

# num = int(input())
# reverse = ''
# while num != 0:
#     last_digit = num % 10
#     reverse += str(last_digit)
#     num //= 10
#
# print(reverse)

# n = int(input())
# last_dight = 0
# max = 0
# min = 9
# while n != 0:
#     last_dight = n % 10
#     if last_dight > max:
#         max = last_dight
#     if last_dight < min:
#         min = last_dight
#     n //= 10
#
# print("Максимальная цифра равна", max)
# print('Минимальная цифра равна', min)


n = int(input())
sum = 0
first = 0
mult = 1
lenght = len(str(n))
last_dight = n % 10
while n != 0:
    last = n % 10
    sum += last
    mult *= last
    if 10 < n < 100:
        first = n // 10
    n //= 10


avg_arifm = sum / lenght


print(sum, lenght, mult, avg_arifm, first, first + last_dight, sep='\n')
