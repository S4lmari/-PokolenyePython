# s = input()
#
# if s == s.title():
#     print('YES')
# else:
#     print("NO")
#
# s = input()
#
# print(s.swapcase())
# s = input()
#
# formated = s.lower()
# if 'хорош' in formated:
#     print("YES")
# else:
#     print("NO")
s = input()
count = 0
for i in range(len(s)):
    if s[i] in "abcdefghijklmnopqrstuvwxyz":
        count += 1
print(count)
