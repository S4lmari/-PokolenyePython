# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i[1:] for i in keywords]
#
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [i for i in keywords if len(i) >= 5]
#
# print(lengths)

# palindromes = [i for i in range(100, 1000) if i // 100 == i % 10]
#
# print(palindromes)

# n = int(input())
#
# square = [print(i**2) for i in range(1,n+1)]

# str = input().split()
#
# kube = [print(int(el)**3,end=" ") for el in str]

# one_str = [print(el) for el in input().split()]

# one_str_2 = [print(e, end='') for el in input().split() for e in el if e in "0123456789"]

square = [print(int(num) ** 2,end=' ') for num in input().split() if int(num) % 2 == 0 and (int(num) ** 2) % 10 != 4]
