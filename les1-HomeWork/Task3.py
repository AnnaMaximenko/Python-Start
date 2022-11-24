# 3.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

numberX = int(input('Введите коордианты X: '))
numberY = int(input('Введите коордианты Y: '))

if numberX == 0 or numberY == 0:
    print("Координаты не должны быть равны 0")

elif numberX > 0 and numberY > 0:
    print("1 четверть")
elif numberX < 0 and numberY > 0:
    print("2 четверть")
elif numberX < 0 and numberY < 0:
    print("3 четверть")
elif numberX > 0 and numberY < 0:
    print("4 четверть")
