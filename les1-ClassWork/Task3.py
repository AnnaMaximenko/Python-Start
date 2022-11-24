# 1.	Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

number_N = int(input("Введите число "))

for i in range(- number_N, number_N+1):
    print(i, end=" ")
