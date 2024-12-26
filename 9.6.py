# In 2010, someone paid 10k Bitcoin for two pizzas.
# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# age = 2010
# summ = "10k"
# token = "Bitcoin"
# text = s.format(age,summ,token)
# print(text)

# Date,Dollar,Yuan = input(),input(),input()
# template = 'На {}: 1$ = {}₽, 1¥ = {}₽'
#
# text = template.format(Date,Dollar,Yuan)
# print(text)

# a, b = int(input()), int(input())
#
# print(f'Для чисел {a} и {b}')
# print(f'  Сумма кубов: {a}**3 + {b}**3 = {a ** 3 + b ** 3}')
# print(f'  Куб суммы: ({a} + {b})**3 = {(a+b)**3}')

day, weight = int(input()), float(input())

target_weight = 100 - day * 0.2
if weight <= target_weight:
    result = "Все идет по плану"
else:
    result = "Что-то пошло не так"
print(result, f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {target_weight} кг',sep="\n")
