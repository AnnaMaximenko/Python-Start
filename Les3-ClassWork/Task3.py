<<<<<<< HEAD
# ; 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел.

import time
# print(str(time.time()))

def my_random(n):
    str_time = str(time.time())
    str_time = str_time.replace('.', '')
    number = int(str_time) % n
    return number

=======
# ; 3.	Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел.

import time
# print(str(time.time()))

def my_random(n):
    str_time = str(time.time())
    str_time = str_time.replace('.', '')
    number = int(str_time) % n
    return number

>>>>>>> 44db217050cb8a047d4eaaaed973a9efe621002e
print(my_random(1000))