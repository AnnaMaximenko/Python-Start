# 6.	Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

n1 = 'vvkjhvvk '
n2 = 'vv'

# print(n1.count(n2))

i = 0
count = 0

while i < len(n1):
    if n1 [i:i + len(n2)] == n2:
        count += 1
        i += (len(n2)-1)
    i +=1

print(count)
