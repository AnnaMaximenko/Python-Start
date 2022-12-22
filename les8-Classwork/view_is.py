
def show_menu():
    print('Выберите команду:\n 1 - показать всех сотрудников \n 2 - добавить сотрудника \n 3 - изменить данные о сотруднике \n 4 - удалить сотрудника \n 5 - импорт csv-файла в txt-файл \n 6 - импорт txt-файла в csv-файл')
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6]:
            raise ValueError
        return (select)
    except Exception:
        print('Ошибка ввода! Выберите номер из списка')
        exit()


def show_employees(sotr):
    print('Список всех сторудников: ')
    for i, sotrudnik in enumerate(sotr):
        if i == 0:
            print(' ', *sotrudnik)
        else:
            print(i, *sotrudnik)


def add_employees():
    info = []
    last_name = ''
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        phone_number = input('Введите номер телефона: ')
        if len(phone_number) != 11:
            print('В номере телефона должно быть 11 цифр.')
        else:
            valid = True
    info.append(phone_number)
    description = input('Введите должность: ')
    info.append(description)
    return info


def change_employees():
    print('Выберите строчку для перезаписи: ')
    change = int(input())
    print('Введите строку: ')
    string = input().split()
    return change, string


def delete_employees():
    print('Выберите строчку для удаления: ')
    change = int(input())
    return change


def print_mode_import_txt():
    print()
    print('Выбран режим импорт в txt-файл')
    print()
    return


def print_import():
    print('Данные импортированы в файл')
    return


def print_mode_output_txt():
    print()
    print('Выбран режим экспорт из txt-файла.')
    print()
    return


def print_output():
    print('Данные импортированы в файл.')
    return
