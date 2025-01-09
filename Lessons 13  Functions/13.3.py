# def swap(a, b):
#     a, b = b, a
#
# a = 4
# b = 3
# swap(a, b)
# print(a - b)
from itertools import count


# --- Функции с возвратом значения ---
# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
#
# print(get_sum(1, 2, 3))

# def convert_to_miles(km):
#     return km * 0.6214
#
#
# num = int(input())
# print(convert_to_miles(num))

# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         days = 31
#     elif month in [4, 6, 9, 11]:
#         days = 30
#     else:
#         days = 28
#     return days
#
# num = int(input())
# print(get_days(num))


# def get_factors(num):
#     nums = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             nums.append(i)
#     return nums
#
# def number_of_factors(num):
#     return len(num)
#
# n = int(input())
# print(number_of_factors(get_factors(n)))

# def find_all(target, symbol):
#     count = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             count.append(i)
#     return count
#
# target = input()
# char = input()
#
# print(find_all(target, char))

# def merge(list1, list2):
#     new_list = list1+list2
#     new_list.sort()
#     return new_list
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

final_list = []
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result


n = int(input())

for i in range(n):
    l = input().split()
    mapped_list = list(map(int,l))
    final_list = quick_merge(final_list,mapped_list)
    l.clear()
print(*final_list)




