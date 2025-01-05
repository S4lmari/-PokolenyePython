# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers += numbers.copy()
# numbers.insert(3, "25")
# print(numbers)

# nums = input().split()
# new_nums = []
# for num in nums:
#     new_nums.append(int(num))
# copy = new_nums.copy()
# index_max = new_nums.index(max(new_nums))
# index_min = new_nums.index(min(new_nums))
#
# new_nums[index_max] = min(copy)
# new_nums[index_min] = max(copy)
# for el in new_nums:
#     print(el,end=' ')

# text = input().lower().split()
#
# count_a = text.count('a')
# count_an = text.count('an')
# count_the = text.count('the')
#
# print(f'Общее количество артиклей: {count_the + count_a + count_an}')

# ---Взлом братства стали (удаление лишних строк)---

# n = [] # это мы поолучили число строк
# n.extend(input())
# del n[0]
# count_str = ''.join(n)
#
# code = [] #принимаю код и заношу его всписок
# for st in range(int(count_str)):
#     code.append(input())
#
# for el in range(len(code)):
#     if "#" in code[el]:
#         index = code[el].find("#")
#         code[el] = code[el][:index].rstrip()
#
# print('\n'.join(code))

sting = input().split()
sting.sort()
revers_str = sting


print(" ".join(sting)," ".join(sting[::-1]),sep="\n")
