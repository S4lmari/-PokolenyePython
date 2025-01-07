# nums = [i for i in range(0, int(input()) + 1, 2)]
# print(nums[1:])

# l = input().split()
# m = input().split()
#
# summ = [int(m[i]) + int(l[i]) for i in range(len(l))]
# for num in summ:
#     print(int(num),end=" ")

# nums = input().split()
# summ = 0
# for i in nums:
#     summ += int(i)
# print(*nums,sep='+',end=f'={summ}')

# --- Проверка номера ---
# phone_number = input()
# a = list(phone_number)
# check = [7,'-',"dig","dig","dig",'-',"dig","dig","dig",'-',"dig","dig","dig","dig"]
# check_2 = ["dig","dig","dig",'-',"dig","dig","dig",'-',"dig","dig","dig","dig"]
# phone = []
# if a[0] == "7":
#     phone.append(7)
#     for el in range(1,len(a)):
#         if a[el] in "0123456789":
#             phone.append("dig")
#         elif a[el] == "-":
#             phone.append('-')
# else:
#     for el in range(len(a)):
#         if a[el] in "0123456789":
#             phone.append("dig")
#         elif a[el] == "-":
#             phone.append('-')
#
# if phone == check or phone== check_2:
#     print("YES")
# else:
#     print("NO")

# text = input().split()
#
# max_len = [len(word) for word in text]
# print(max(max_len))

print(*[word[1:] + word[0] + 'ки' for word in input().split()])
