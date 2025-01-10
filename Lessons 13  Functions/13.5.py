# def is_valid_triangle(a, b, c):
#     ab = a+b
#     ac = a+c
#     bc = b+c
#     if ab>c and ac>b and bc>a:
#         return  True
#     else:
#         return False
#
# a, b, c = int(input()), int(input()), int(input())
#
# print(is_valid_triangle(a, b, c))
from itertools import count


# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#             break
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False


# n = int(input())
#
# print(is_prime(n))


# def get_next_prime(num):
#     while True:
#         num += 1
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             return num
#
#
# n = int(input())
# print(get_next_prime(n))


# def is_password_good(password):
#     if len(password) >= 8:
#         flag1 = False
#         flag2 = False
#         flag3 = False
#
#         for i in password:
#             if i.isupper():
#                 flag1 = True
#             elif i.islower():
#                 flag2 = True
#             elif i.isdigit():
#                 flag3 = True
#         if flag1*flag2*flag3 == 1:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# txt = input()
# print(is_password_good(txt))


# def is_one_away(word1, word2):
#     if len(word1) == len(word2):
#         count = 0
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 count += 1
#         if count == 1:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# txt1 = input()
# txt2 = input()
#
# print(is_one_away(txt1, txt2))


# def is_palindrome(text):
#     text = text.strip().lower()
#     text_without = ""
#     for i in text:
#         if i.isalpha():
#             text_without += i
#     if text_without == text_without[::-1]:
#         return True
#     else:
#         return False
#
# txt = input()
# print(is_palindrome(txt))


# def is_valid_password(password):
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     flag4 = False
#
#     pas = password.split(":")
#     if len(pas) == 3:
#         flag4 = True
#     if pas[0] == pas[0][::-1]:
#         flag1 = True
#     if is_prime(int(pas[1])):
#         flag2 = True
#     if int(pas[2]) % 2 == 0:
#         flag3 = True
#
#     if flag1 * flag2 * flag3 * flag4 == 1:
#         return True
#     else:
#         return False
#
#
# psw = input()
# print(is_valid_password(psw))


# def is_correct_bracket(text):
#     count = 0
#     for braket in text:
#         if braket == "(":
#             count += 1
#         elif braket == ")":
#             count -= 1
#
#         if count < 0:
#             break
#     if count == 0:
#         return True
#     else:
#         return False
#
# txt = input()
# print(is_correct_bracket(txt))


def convert_to_python_case(text):
    python_text = ""
    for letter in text:

        if letter == letter.upper() and not letter.isdigit() == True:
            python_text += f'_{letter.lower()}'
        else:
            python_text += letter
    return python_text[1:]


txt = input()
print(convert_to_python_case(txt))
