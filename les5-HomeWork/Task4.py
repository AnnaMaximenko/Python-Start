# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

# Файл 1
# Текст после кодировки: 12W1B12W3B24W1B14W
# Файл 2
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Файл 3
# Входные и выходные данные хранятся в отдельных текстовых файлах.

path = 'file_les5HW.txt'
data = open(path, 'r')

a=data.read()
print(a)

data.close()

count = 1
res=  ''

for i in range(1,len(a)-1):
    if a[i]==a[i+1]:
        count +=1
    else:
        res = res + str(count) + a[i]
        count = 1
if count > 1 or (a[len(a)-2] != a[-1]):
        res = res + str(count) + a[-1]
print (res)

path1 = 'file_les5HWZAP.txt'
data1 = open(path1, 'w')

a=data1.write(res)
data.close()





number = ''
result = ''
for i in range(len(res)):
    if not res[i].isalpha():
        number += res[i]
    else:
        result = result + res[i] * int(number)
        number = ''
print(result) 

path2 = 'file_les5HWZAP1.txt'
data2 = open(path2, 'w')

a=data2.write(res)
data.close()

