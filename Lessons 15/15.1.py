# ---Числовая угадайка---
import random

def is_valid(n): # проверка на соответствие введенного значения условию
    return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100

def input_num(): # ввод данных
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def compare_num(down_num, up_num): # Сравнение введенного значения с загаданным
    num = random.randint(down_num, up_num)
    total = 0
    while True:
        n = input_num()
        total += 1
        if n < num:
            print('Не угадали, попробуйте число побольше')
        elif n > num:
            print('Мимо, назовите число поменьше')
        else:
            print('Победа!!! Вы угадали ответ за', total,  'попыток, поздравляем!' )
            break

def continue_game(): # Предложение продолжить игру
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return True

def game(): # Запуск игры
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
        x, y = input_num(), input_num()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare_num(x, y)
        if continue_game():
            continue
        else:
            break

game() # Вызов игры