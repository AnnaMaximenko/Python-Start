# 2.	Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

number = int(input('Введите число N: '))


i = 2 
list = []

while i <= number:
    if number % i == 0:
        list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print("Простые множители:",*list)