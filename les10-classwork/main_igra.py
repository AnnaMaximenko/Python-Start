import logging
import token_bot
import emoji

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

candies = 150
step = 28
count_bot = 0
count_player = 0


reply_keyboard = [['/play', '/settings'],
                  ['/rules', '/close']]

reply_keyboard_stop = [['/start', '/stop']]


markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup_stop = ReplyKeyboardMarkup(reply_keyboard_stop, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)


logger = logging.getLogger(__name__)

TOKEN = token_bot.token


def start(update, context):
    name = f'{update.message.from_user.first_name}{update.message.from_user.last_name}'
    update.message.reply_text(emoji.emojize(
        f"Привет, :red_heart: {name}! :red_heart: Давай поиграем? Выбери пункт:"),
        reply_markup=markup,
    )


def close_keyboard(update, context):
    update.message.reply_text(emoji.emojize(
        'До скорой встречи :thumbs_up:'),
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "В начале игры на столе лежит определенное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем определенное количество конфет. Все конфеты оппонента достаются сделавшему последний ход.")


def settings(update, context):
    update.message.reply_text(
        'Введите количество конфет на столе и максимальное возможное количество конфет, которые можно взять за один ход: ')
    return 1


def set_settings(update, context):
    global candies
    global step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text('Правила установлены')
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(
        f'Ваш ход. На кону {candies} конфет. Какое количество конфет возьмете?' f'(Максимальное количество конфет на ход = {step})', reply_markup=ReplyKeyboardRemove())

    return 1


def play_step(update, context):
    global count_bot
    global count_player
    global candies
    candiy = int(update.message.text)
    count_player = count_player+1
    candies -= candiy
    if candiy > step:
        update.message.reply_text(
            f'Ты ввел конфет больше, чем {step}. Не нарушай правила игры. Введи правильное количество конфет')
    elif candies < step:
        update.message.reply_text(
            f'Игра закончена. Я забираю оставшиеся конфеты.Я победил всего за {count_bot} шага')
        update.message.reply_text(
            f'Если хочешь играть еще раз выбери start. Для выхода выбери stop', reply_markup=markup_stop)
        return ConversationHandler.END
    else:
        update.message.reply_text(
            f'На кону {candies} конфет, я беру {candies%(step+1)} конфет')
        update.message.reply_text(
            'Сколько возьмёшь ты?')
        candies -= candies % (step+1)
        count_bot = count_bot+1

        if candies <= step:
            update.message.reply_text(
                f'Поздравляю! Ты победил! Тебе понадобилось всего {count_player} шага', reply_markup=markup)
            update.message.reply_text(
                f'Если хочешь играть еще раз выбери start. Для выхода выбери stop', reply_markup=markup_stop)
            return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    settings_handler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(settings_handler)
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("stop", stop))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
