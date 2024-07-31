# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)
# print("*" * 17)
# print("*", "*", sep=(" " * 15))
# print("*", "*", sep=(" " * 15))
# print("*" * 17)

# a = int(input())
# b = int(input())
# kvadrat_summ = (a + b) ** 2
# summ_kvadtat = a ** 2 + b ** 2
# print("Квадрат суммы", a, "и", b, "равен", kvadrat_summ)
# print("Сумма квадратов", a, "и", b, "равна", summ_kvadtat)
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# summ = a ** b + c ** d
# print(summ)


n = int(input())
if 1 <= n <= 9:
    s = n
    d = str(n) + str(n)
    e = str(n) + str(n) + str(n)
    print(s + int(d) + int(e))
