import view_is
import model_is
import logging

logging.basicConfig(level=logging.INFO)


def main():
    select = view_is.show_menu()
    if select == 1:
        logging.info("Выбрана команда 1")
        sotr = model_is.get_lists()
        view_is.show_employees(sotr)
        logging.info('Команда 1 сработала')
    elif select == 2:
        logging.info("Выбрана команда 2")
        data = view_is.add_employees()
        model_is.add_employees_to_list(data)
        logging.info('Команда 2 сработала')
    elif select == 3:
        logging.info("Выбрана команда 3")
        change, string = view_is.change_employees()
        model_is.update_employees(change, string)
        logging.info('Команда 3 сработала')
    elif select == 4:
        logging.info("Выбрана команда 4")
        change = view_is.delete_employees()
        model_is.delete(change)
        logging.info('Команда 4 сработала')
    elif select == 5:
        logging.info("Выбрана команда 5")
        view_is.print_mode_import_txt()
        model_is.data_output_txt()
        logging.info('Данные импортированы в txt-файл')
        view_is.print_import()
    elif select == 6:
        logging.info("Выбрана команда 6")
        view_is.print_mode_output_txt()
        model_is.data_input_txt()
        logging.info('Данные импортированы в csv-файл')
        view_is.print_output()
    logging.info("Программа отработала корректно")
