# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки. 
# Входные данные	Выходные данные
# 36
# 12
# 144
# 18	6

import math
print('Ввод чисел продолжается до ввода пустой строки')
print()

def int_input():
    while True:
        try: yield int(input('Введите число: '))
        except ValueError: break

x, y, *z = int_input()
print(f'Список введенных чисел: {x, y, *z}')

result = math.gcd(x, y, *z)
print(f'Наибольший общий делитель: {result}')