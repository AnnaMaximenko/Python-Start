# 2.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

firstDigit = 1
n = int(input('Введите число N: '))

for i in range (n):
    firstDigit *= i+1
    print(firstDigit, end=' ')

