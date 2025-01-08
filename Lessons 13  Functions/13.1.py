# def draw_box():
#     print("*" * 10)
#     for _ in range(12):
#         print("*", "*", sep=' ' * 8)
#     print("*" * 10)
#
#
# draw_box()  # вызов функции


# def draw_triangle():
#     for i in range(1,11):
#         print(i*"*")
# draw_triangle()  # вызов функции

# объявление функции
# def draw_triangle(fill, base):
#     for i in range(1,(base // 2)+2):
#         print(i * fill)
#     for j in range(base // 2, 0, -1):
#         print(j * fill)
#
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)

# объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(),name[0].upper(),patronymic[0].upper(),sep='')
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# объявление функции
def print_digit_sum(num):
    summ = 0
    for i in str(num):
        summ += int(i)
    print(summ)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
