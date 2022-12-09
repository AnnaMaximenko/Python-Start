<<<<<<< HEAD
# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# (встроенными методами пользоваться нельзя).
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10

input_number = int(input("Введите число для преобразовывания: "))
output_number = str()

while input_number != 0:
    output_number = str(input_number%2) + output_number
    input_number //=2
    
print(output_number)

=======
# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# (встроенными методами пользоваться нельзя).
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10

input_number = int(input("Введите число для преобразовывания: "))
output_number = str()

while input_number != 0:
    output_number = str(input_number%2) + output_number
    input_number //=2
    
print(output_number)

>>>>>>> 44db217050cb8a047d4eaaaed973a9efe621002e
