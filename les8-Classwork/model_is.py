import csv
import logging


def get_lists():
    with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        # title = next(reader)
        # for row in reader:
        # print(row)
        # Если заголовок нужен, то оставляем строки выше
        logging.info('Сработало')
        return list(reader)


def add_employees_to_list(employees):
    with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', 'a', encoding='utf8', newline='') as csvfile:
        # запись в файл, для перезаписи режим 'w'
        writer = csv.writer(csvfile, delimiter=';')
        # row =['колбаса',500,'микоян']
        # writer.writerow(row)
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', 'r', encoding='utf8', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string
        with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', 'w', encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print('Вы вышли за границы массива')
        exit()
    except Exception:
        print('Ошибка ввода')
        exit()


def delete(number):
    with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', 'r', encoding='utf8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number-1]
    with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)


def data_output_txt():
    output = open(
        r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.txt', 'a', encoding='utf-8')
    with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', "r", encoding='utf8') as f:
        for row in f:
            output.write(row)


def data_input_txt():
    input = open(
        r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.csv', 'a', encoding='utf-8')
    with open(r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les8-Classwork\file_is.txt', "r", encoding='utf8') as file:
        for row in file:
            input.write(row)
