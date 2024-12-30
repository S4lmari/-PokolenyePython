# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)
#
# # [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers), numbers[-1], numbers[::-1], "YES" if 5 and 17 in numbers else "NO", sep='\n')
# del numbers[0]
# del numbers[-1]
# print(numbers)

# n = int(input())
# element = []
# for i in range(n):
#     el = input()
#     element.append(el)
# print(element)

# alpaphet = []
# for i in range(1, 27):
#     alpaphet.append(chr(96 + i) * i)
# print(alpaphet)

# n = int(input())
# numbers = []
# for i in range(n):
#     num = int(input())
#     numbers.append(num ** 3)
# print(numbers)

# n = int(input())
# nums = []
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         nums.append(i)
# print(nums)

# n = int(input())
# nums = []
# summ_nums = []
# for i in range(n):
#     nums.append(int(input()))
# for j in range(len(nums)):
#     summ_nums.append(nums[j] + nums[j - 1])
# del summ_nums[0]
# print(summ_nums)
#
# n = int(input())
# nums = []
# del_nums = []
# for i in range(n):
#     nums.append(int(input()))
# # for j in range(n):
# #     if j % 2 != 0:
# #         del_nums.append(j)
# # print(nums)
# # del nums[del_nums[0]:del_nums[-1]+1]
# # print(nums)
# del nums[1::2]
# print(nums)

# n = int(input())
# list = []
# new_lsit = []
# new_word = ''
# for i in range(n):
#     list.append(input())
# k = int(input())
#
# for j in list:
#     if len(j)>=k:
#         print(j[k-1],end='')
#     else:
#         continue

n = int(input())
list = []
for i in range(n):
    list.extend(input())
print(list)