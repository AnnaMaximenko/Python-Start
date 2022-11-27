# 5.	Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).

test_list = [1, 2, 3, 4, 5]

import random 
print ("Оригинальный список: " + str(test_list))
 
for i in range(len(test_list)-1, 0, -1):
        j = random.randint(0, i + 1)    
        test_list[i], test_list[j] = test_list[j], test_list[i]     

print ("Перемешанный список : " +  str(test_list))