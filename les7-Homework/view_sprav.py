def greeting ():
    print('Hello! Выберите формат для работы 1 - txt, 2 - csv ')
    select = int(input())
    return select


def choice ():
    print('Выберите процесс 1 - импорт, 2 - экспорт ')
    choose = int(input())
    return choose


def input_txt():
    info = []
    last_name = ''
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:        
        phone_number = input('Введите номер телефона: ')
        if len(phone_number) != 11:
            print('В номере телефона должно быть 11 цифр.')
        else:            
            valid = True       
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info


def print_import():
    print('Данные импортированы в файл')
    return


def print_mode_import_txt():
    print()
    print('Выбран режим импорт в txt-файл.Вводите данные на английском языке')
    print()
    return


def print_mode_output_txt():
    print()
    print('Выбран режим экспорт из txt-файла.')
    print()
    return


def print_output():
    print('Данные экспортированы.')
    return


def print_mode_import_csv():
    print()
    print('Выбран режим импорт в csv-файл.Вводите данные на английском языке')
    print()
    return
    

def print_mode_output_csv():
    print()
    print('Выбран режим экспорт из csv-файла.')
    print()
    return




