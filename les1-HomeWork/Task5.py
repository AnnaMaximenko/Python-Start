# 5.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
PointAbyX = float(input('Введите координаты точки a по оси x: '))
PointAbyY = float(input('Введите координаты точки a по оси y: '))

PointBbyX = float(input('Введите координаты точки b по оси x: '))
PointBbyY = float(input('Введите координаты точки b по оси y: '))


distance = math.sqrt((PointBbyX - PointAbyX)**2 + (PointBbyY - PointAbyY)**2)
distance = round(distance, 3)


print(f'Расстояние между точками в 2D пространстве = {distance}')
