<<<<<<< HEAD
# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input('Введите длину ряда: '))


 
def get_fibonacci(number):
    fibo_nums = []
    f1, f2 = 1, 1
    for i in range(number):
        fibo_nums.append(f1)
        f1, f2 = f2, f1 + f2
    f1, f2 = 0, 1

    for i in range (number+1):
        fibo_nums.insert(0, f1)
        f1, f2 = f2, f1 - f2
    return fibo_nums

fibo_nums = get_fibonacci(number)
print(get_fibonacci(number))
=======
# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input('Введите длину ряда: '))


 
def get_fibonacci(number):
    fibo_nums = []
    f1, f2 = 1, 1
    for i in range(number):
        fibo_nums.append(f1)
        f1, f2 = f2, f1 + f2
    f1, f2 = 0, 1

    for i in range (number+1):
        fibo_nums.insert(0, f1)
        f1, f2 = f2, f1 - f2
    return fibo_nums

fibo_nums = get_fibonacci(number)
print(get_fibonacci(number))
>>>>>>> 44db217050cb8a047d4eaaaed973a9efe621002e
