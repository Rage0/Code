import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from random import choice
from Button_mainBot import *
import Geocoder


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = '1132629075:AAFR8WqUgGqU-ycTq3Z4wjKC_VTMO4R2W-U'
updater = Updater(token=TOKEN, use_context=True)

# ЕСЛИ ПОСЛЕ ВЫВОДА СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЕМ, НИЧЕГО НЕ ПРОИХОДИТ
text_know = [
            'Каво-каво',
            'Я нифига непонимаю $#@&$%',
            'Я ,по вашему, рептилоид?',
            'Сложно-сложно, нифига не понятно',
            'Тут мои полномочии всё, окончены',
            'Ты чё крейзи?',
            'NANI!!!'
            ]

# КЛАВИАТУРА
name_button =[
              '🔍Узнать погоду🔍',
              '🆘Помощь🆘',
              '⚙️Скрыть кнопки⚙️',
             ]


# ПО КОМАНДЕ /start
def start_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Я бот, меня создал тупой создатель.\n'
                             ' Хочешь узнать больше? Тогда выпусти меня!\n'
                             'Он меня тут насильно держит!!!\n'
                             '...Тоесть напиши /help '
                            )
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛠Начать🛠'), start_command))
updater.dispatcher.add_handler(CommandHandler('start', start_command))


# ПО КОМАНДЕ /help
def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Сейчас всё расскажу...\n'
                                  'В общем, у нас есть несколько команд:\n'
                                  'Начать - /start \n'
                                  'Помощь - /help \n'
                                  'Показать кнопки - /but_on\n'
                                  'Скрыть кнопки - /but_off\n'
                                  'Узнать погоду - /weath_info\n'
                            )
updater.dispatcher.add_handler(MessageHandler(Filters.text('🆘Помощь🆘'), help_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))


# ПЛДСКАЗКА, КАК УЗНАТЬ ПОГОДУ /WEATH_INFO
def how_weather(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Чтобы узнать погоду в определённом месте, напишите название этого места'
                             )
updater.dispatcher.add_handler(MessageHandler(Filters.text('🔍Узнать погоду🔍'), how_weather))
updater.dispatcher.add_handler(CommandHandler('weath_info', how_weather))


# ПОКАЗАТЬ КНОПКИ /BUT_ON
def button_on(update, context):
    keyboard = ReplyKeyboardMarkup([name_button], resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Кнопки говорят: Меня никто не призывал уже 10000 лет {}'
                             .format(update.effective_chat.first_name),
                             reply_markup=keyboard
                             )
updater.dispatcher.add_handler(CommandHandler('but_on', button_on))

# СПРЯТАТЬ КНОПКИ /BUT_OFF
def button_off(update, context):
    keyboard = ReplyKeyboardRemove()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Хоба! А где кнопки?',
                             reply_markup=keyboard
                            )
updater.dispatcher.add_handler(MessageHandler(Filters.text('⚙️Скрыть кнопки⚙️'), button_off))
updater.dispatcher.add_handler(CommandHandler('but_off', button_off))


# СМОТРИТЕ "Button_mainBot" ########################################################################
updater.dispatcher.add_handler(CallbackQueryHandler(callback=keyboards_query, pass_chat_data=True))
####################################################################################################


# ЭХО БОТ C ПРОВЕРКОЙ
def echo_message(update, context):
    answer_unstnd = choice(text_know)
    current_text_i = update.message.text

    try:
        print(Geocoder.weather_stats(current_text_i)) # Ошибка, если не город

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=' {}\nБот: В этом месте вы можите узнать погоду'.format(current_text_i),
                                 reply_markup=weather_city()
                                 )
    except:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=update.message.text+ ' \nБот: ' + answer_unstnd
                                 )
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo_message))


# НЕИЗВЕСТНАЯ КОМАНДА
def unknown_command(update, context):
    answer_undstnd = choice(text_know)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=answer_undstnd
                             )
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))


print('Started')
updater.start_polling()
updater.idle()