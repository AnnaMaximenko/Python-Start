# 4.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k: '))
list = []

while k >= 0:
    if k > 1:
        koef = randint(0, 100)
        list.append(f'{koef}x^{k} +')
    elif k == 1:
        koef = randint(0, 100)
        list.append(f'{koef}x +')
    else:
        koef = randint(0, 100)
        list.append(f'{koef}')
    k -= 1
list.append("= 0")

print(*list, end="")

lst = ''.join(list)

with open('Task4.txt', 'a') as data:
    data.write(f"{lst}\n")
