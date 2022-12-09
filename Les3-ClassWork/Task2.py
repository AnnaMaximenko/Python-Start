<<<<<<< HEAD
#  2.	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

list = [1,5,2,4,3]
new_list = []

for i in range(len(list) - 1):
    if list[i] < list [i+1]:
        new_list.append(list[i+1])
=======
#  2.	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

list = [1,5,2,4,3]
new_list = []

for i in range(len(list) - 1):
    if list[i] < list [i+1]:
        new_list.append(list[i+1])
>>>>>>> 44db217050cb8a047d4eaaaed973a9efe621002e
print(*new_list)