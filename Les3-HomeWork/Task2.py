<<<<<<< HEAD
# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]


list = [2, 3, 5, 6]



def mult_list(list):
    if len(list) % 2 != 0:
        list2 = len(list) //2 +1
    else: 
        len(list)//2
        list2 = len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(list2)]
    print(new_list)


mult_list(list)












=======
# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]


list = [2, 3, 5, 6]



def mult_list(list):
    if len(list) % 2 != 0:
        list2 = len(list) //2 +1
    else: 
        len(list)//2
        list2 = len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(list2)]
    print(new_list)


mult_list(list)












>>>>>>> 44db217050cb8a047d4eaaaed973a9efe621002e
