# 3.	Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

def flolist(list):
    newlist = []
    for i in list:
        if type(i) is float:
            newlist.append(i)
    return newlist

newlist = flolist(list)

def divaid(newlist):
    newlist2 = []
    for i in newlist:
        j = i - int(i)
        newlist2.append(j)
    return newlist2

newlist2 = divaid(newlist)

def max(newlist2):
    max = newlist2[0]
    for i in range(len(newlist2)):
        if max < newlist2[i]:
            max = newlist2[i]
    return(max)

def min(newlist2):
    min = newlist2[0]
    for i in range(len(newlist2)):
            if min > newlist2[i]:
                min = newlist2[i]
    return(min)
   

max = max(newlist2)
min = min(newlist2)

number = max - min
print(round(number,2))

