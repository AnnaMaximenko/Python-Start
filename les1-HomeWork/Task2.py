# 2.	Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for numberX in True, False:
    for numberY in True, False:
        for numberZ in True, False:
            print(f'Результат : {not(numberX or numberY or numberZ) == (not numberX and not numberY and not numberZ)}')

