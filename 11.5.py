# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)
from itertools import count

# st = input()
# text = st.split()
#
# print("\n".join(text))

# st = input().split()
# for i in st:
#     print(i[0],end='.')

# st =input().split('\\')
# for el in st:
#     print(el)

# numders = input().split()
# for el in numders:
#     print(int(el) * "+")

# ip = input().split('.')
# flag = None
# for el in ip:
#     if int(el) not in range(255):
#         flag = False
#         break
#     else:
#         flag = True
# if flag == True:
#     print("ДА")
# else:
#     print("НЕТ")

# st = input()
# separate = input()
#
# print(separate.join(st))

nums = input().split()
count = 0

for num in nums:
    if nums.count(num) == 2:
        count += 1
        nums.remove(num)
    elif nums.count(num) > 2:
        count += nums.count(num) * 1 - 0.5
        nums.remove(num)
    else:
        nums.remove(num)

print(int(count))
