a=5 #int
b="hhjj" #str
c=0.5 #float
t=True #bool

#объявляем тип

# if a>4:
#     print(a)
# elif a<0:
#     print(0)
# else:
#     print("FFFF")

# цикл if

# for i in range(5):
#     print("Mama")

# цикл for

# while i<5:
#     print("Mama")
#     i +=1

# цикл while

# Создание списка:

# sp = list() 
# # или
# # sp=[]
# sp.append(5)
# sp.append(8)
# print(sp)

# # Обращаемся к списку

# sp =[1,5,3,89,3]
# print(sp [0])
# print(sp [-1])

# Перебор элементов списка

sp = [1, 5, 89, 3, 3]
for i in range(0, len(sp)):
    print (sp[i], end=" ")
print()
# этот способ лучше использовать если хотим что-то изменить

for el in sp:
    print(el, end=' ')
# этот способ лучше использовать при печати

print(sp)
# напечатает в квадратных скобках

print(*sp)
# напечатает без скобок