# 2.	Определите среднее значение всех элементов последовательности, завершающейся числом 0.

print('Введите числа, по окончанию введите 0')
n = None
# sum = 0
# count = 0

# while n != 0:
#     n = int(input())
#     count += 1
#     sum += n

# count -= 1
# print(round (sum / count, 2))

sp = []
while n != 0:
    n = int(input())
    sp.append(n)

print(round(sum(sp) / (len(sp) - 1),2))
