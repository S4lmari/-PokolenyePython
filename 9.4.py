# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))
# s = input()
#
# print(s.count(" ")+1)
from itertools import count

# s = input()
# x = s.lower()
#
# print('Аденин:',x.count("а"))
# print('Гуанин:',x.count("г"))
# print('Цитозин:',x.count("ц"))
# print('Тимин:',x.count("т"))

# n = int(input())
# count = 0
# for i in range(n):
#     s = input()
#     if s.count("11") >= 3:
#         count += 1
# print(count)

# s = input()
# count = 0
#
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         count += 1
# print(count)
# text = input()
# cnt = 0
#
# for i in range(10):
#     cnt += text.count(str(i)) # Счетчик работает на цифры в цикле 35 строки. КНТ прибавляет если есть i цифра
#
# print(cnt)

# s = input()
# if s.endswith(".com") or s.endswith(".ru"):
#     print("YES")
# else:
#     print("NO")

# s = input()
#
# max = 0
#
# for i in s:
#     if s.count(i) >= max:
#         max = s.count(i)
#         symbol = i
# print(symbol)

# s = input()
#
# if s.count("f") == 1:
#     print(s.find("f"))
# elif s.count("f") > 1:
#     print(s.find("f"),s.rfind("f"))
# else:
#     print("NO")

s = input()

first = s.find("h")
last = s.rfind("h")
print(s[:first],s[last+1:],sep="")