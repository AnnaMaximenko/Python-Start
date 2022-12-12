# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно 
# взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a)	Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

# Игра с человеком

candies = 100
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")

flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первым ходит {player1}")
else:
    print(f"Вторым ходит {player2}")


def input_dat(name):
    x = int(input(f"{name} введите количество конфет: "))
    while x < 1 or x > 28:
        x = int(input("За один ход можно взять не более 28 конфет, введите корректное количество конфет: "))
    return x


while candies>28:
    print(f'Ход {player1} ')   
    number = input_dat(player1)    
    candies = candies - number
    print('Осталось конфет: ',candies)
    if candies< 28:
        print(f'Победил {player1}')
    else:
        print(f'Ход {player2}')   
        number = input_dat(player1)    
        candies = candies - number
        print('Осталось конфет: ',candies)
        if candies< 28:
            print(f'Победил {player2}')  

# Игра с ботом

# candies = 100
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите для бота: ")

# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первым ходит {player1}")
# else:
#     print(f"Вторым ходит бот {player2}")


# def input_dat(name):
#     x = int(input(f"{name} введите количество конфет: "))
#     while x < 1 or x > 28:
#         x = int(input("За один ход можно взять не более 28 конфет, введите корректное количество конфет: "))
#     return x


# while candies>28:
#     print(f'Ход {player1} ')   
#     number = input_dat(player1)    
#     candies = candies - number
#     print('Осталось конфет: ',candies)
#     if candies< 28:
#         print(f'Победил {player1}')
#     else:
#         print(f'Ход бота {player2}')   
#         number = randint(1,29)
#         print(f'Количество взятых конфет: {number}')    
#         candies = candies - number
#         print('Осталось конфет: ',candies)
#         if candies< 28:
#             print(f'Победил бот {player2}')  


