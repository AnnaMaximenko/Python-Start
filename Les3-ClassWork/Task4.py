# ; 4.	Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# list = []
# number = 12
# f = 0
# print ("Введите элементы списка: ")

# for i in range(5):
#     list.append(input())

# for i in range(5):
#     if list[i] == str(number):
#         # if str(number) in list[i] если в элементе есть number
#         f = 1
# if f:
#     print('Yes')
# else:
#     print('No')

print ("Введите элементы списка: ")
list =[]

for i in range(5):
    list.append(input())
if any('12' in el for el in list):
    print('Yes')
else:
    print('No')




