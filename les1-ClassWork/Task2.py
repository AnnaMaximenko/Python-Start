# 2.	Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

num = 0
number = int(input('Введите число '))
max_num = number

while num < 4:

    number = int(input('Введите число '))
    if number > max_num:
        max_num = number
    num += 1

print(max_num)

# # Var2

# sp = list()
# for i in range(5):
#     n = int(input())
#     sp.append(n)
# print(max(sp))
