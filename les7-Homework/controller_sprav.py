import view_sprav
import logging
import model_sprav
import csv

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding='utf-8')


def main_function():
    try:
        select = view_sprav.greeting()
        if select == 1:
            logging.info('Выбран режим txt')            
            select = view_sprav.choice()
            try:
                if select == 1:
                    logging.info('Выбран режим импорт')
                    view_sprav.print_mode_import_txt()
                    introduction_txt = view_sprav.input_txt()                    
                    model_sprav.data_entry_txt(introduction_txt)
                    logging.info('Данные импортированы в файл')
                    view_sprav.print_import()                    
                elif select == 2:
                    logging.info('Выбран режим экспорт')
                    view_sprav.print_mode_output_txt()
                    print (model_sprav.data_output_txt())
                    view_sprav.print_output()
            except Exception as err: 
                logging.warning(f'Введено некорректное значение {err}')
                
        elif select == 2:
            logging.info('Выбран режим csv')            
            select = view_sprav.choice()
            try:
                if select == 1:
                    logging.info('Выбран режим импорт')
                    view_sprav.print_mode_import_csv()
                    introduction_csv = view_sprav.input_txt()
                    model_sprav.data_entry_csv(introduction_csv)
                    logging.info('Данные импортированы в файл')
                    view_sprav.print_import()
                elif select == 2:
                    logging.info('Выбран режим экспорт')
                    view_sprav.print_mode_output_csv()
                    print (model_sprav.data_output_csv())
                    view_sprav.print_output()
            except Exception as err: 
                logging.warning(f'Введено некорректное значение {err}')   
    except Exception as err: 
        logging.warning(f'Введено некорректное значение {err}')