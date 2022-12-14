# Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится лук. Переписывайте без него.

# Формат ввода
# На первой строке вводится натуральное число N — количество пунктов рецепта.
# Далее следуют N строк — пункты рецепта.

# Формат вывода
# Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием лука (то есть таких, 
# в которых нет подстроки "лук" в нижнем регистре).

# ввод
# 5
# лук 1 головка
# картофелин штук 6
# картошку почистить
# лук порезать кольцами
# зажарить всё

# вывод
# картофелин штук 6, картошку почистить, зажарить всё

n = 5
sp = []

for i in range(1,6):
    sp.append(input())
print(sp)

sp= list(filter(lambda x: 'лук' not in x,sp))
sp.sort(key= lambda x: len (x))
# print(*sp, sep = ',')

print(', '.join(sp))