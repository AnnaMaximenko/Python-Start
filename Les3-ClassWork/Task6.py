# 3.	Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:

MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..'}

print('Введите сообщение: ')

stroka = input().upper().split()
# сплит сделал из строки список

for i in stroka:
    for bukva in i:
        if bukva in MORSE:
            print(MORSE[bukva], end="")
            # обращаемся к значению по ключу
    print()




