from token_bot import token
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import logging
import sqlite3
TOKEN = token

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text(
        "Добро пожаловать. Выберите команду: \n/show - Показать контакты\n/create - Создать новый контакт\n/search - Поиск контакта\n/delete - Удалить контакт"
        "\nВы можете прервать бота, послав команду /stop.\n")


def show(update, context):
    sqlite_connection = sqlite3.connect(
        r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les9-Homework\phone.db3')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from people"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for i in range(len(records)):
        update.message.reply_text(
            ''.join("ID:" + str(records[i][0]) + '\n' + "Фамилия:" + str(records[i][1]) + '\n'+"Имя:" + str(records[i][2]) + '\n'+"Телефон:" + str(records[i][3]) + '\n'+"Должность:" + str(records[i][4]) + '\n'))
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def create_abonent(update, context):
    conn = sqlite_connection = sqlite3.connect(
        r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les9-Homework\phone.db3')
    cursor = sqlite_connection.cursor()
    first_name, name, phone, description = update.message.text.split()
    cursor.execute("select * from people")
    cursor.execute(
        f"insert into people (surname, name, phone, description) "
        f"values ('{first_name}', '{name}', '{phone}','{description}')")
    conn.commit()
    update.message.reply_text("Контакт добавлен")
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def create(update, context):
    update.message.reply_text(
        "Введите Фамилию имя телефон должность через пробел: ")
    return 1


def search(update, context):
    update.message.reply_text("Введите фамилию:  ")
    return 1


def search_abonent(update, context):
    conn = sqlite_connection = sqlite3.connect(
        r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les9-Homework\phone.db3')
    cursor = sqlite_connection.cursor()
    fl = 0
    surname = update.message.text
    if surname != surname.title():
        update.message.reply_text(
            'Введите фамилию с заглавной буквы')
        surname = update.message.text
    elif surname == surname.title():
        cursor.execute(f"select surname from people")
        records = cursor.fetchall()
        for elements in records:
            if surname in elements:
                cursor.execute(
                    f"select * from people where surname like '%{surname}%'")
                records = cursor.fetchall()
                fl = 1
                for i in range(len(records)):
                    update.message.reply_text(
                        ''.join("ID:" + str(records[i][0]) + '\n' + "Фамилия:" + str(records[i][1]) + '\n'+"Имя:" + str(records[i][2]) + '\n'+"Телефон:" + str(records[i][3]) + '\n'+"Должность:" + str(records[i][4]) + '\n'))
                    update.message.reply_text("Всего доброго!")
                    return ConversationHandler.END


def delete(update, context):
    update.message.reply_text("Введите ID контакта для удаления:")
    return 1


def delete_contact(update, context):
    id = update.message.text
    conn = sqlite_connection = sqlite3.connect(
        r'C:\Users\zheka\OneDrive\Рабочий стол\Pyton\les9-Homework\phone.db3')
    cursor = sqlite_connection.cursor()
    cursor.execute(
        f"delete from people where ID='{id}'"
    )
    conn.commit()
    update.message.reply_text("Контакт удален")
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    show_handler = CommandHandler('show', show)
    create_handler = ConversationHandler(
        entry_points=[CommandHandler('create', create)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, create_abonent)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    search_handler = ConversationHandler(
        entry_points=[CommandHandler('search', search)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, search_abonent)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, delete_contact)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)
    dp.add_handler(show_handler)
    dp.add_handler(create_handler)
    dp.add_handler(search_handler)
    dp.add_handler(delete_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
