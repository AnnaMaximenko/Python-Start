# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

number = int(input('Введите число: '))
list = []

index = 0
# position = [2, 5, 1, 3]
position = [int(i) for i in open('les2-HomeWork/file.txt','r')]

for i in range(number):
    list.append(random.randint(-number,number))
print(list)

print(position)

for i in range(len(list)):
    mult = list[position[0] -1]*list[position[1] - 1]*list[position[2] - 1]*list[position[3] - 1]



print(f'Произведение элементов: {list[position[0] -1]} * {list[position[1] - 1]} * {list[position[2] - 1]} * {list[position[3] - 1]} =', mult)




