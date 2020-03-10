from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram import Update
import Geocoder

def weather_city():
    keyboard = [
        [
            InlineKeyboardButton('🌦Погода🌦', callback_data='WEATHER'),
            InlineKeyboardButton('📌Найти место📌', callback_data='GEOLOCATION')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def weather_list():
    keyboard = [
        [
            InlineKeyboardButton('☁️Статус☁️', callback_data='STATUS'),
            InlineKeyboardButton('🌡Температура🌡', callback_data='TEMPERATURE'),
            InlineKeyboardButton('🌪Скорость🌪', callback_data='SPEED_WIND'),
        ],
        [
            InlineKeyboardButton('❌Ничего❌', callback_data='NOTHING')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# ДЕЙСТВИЕ ЗАПРОСОВ
def keyboards_query(update: Update, context):

    query = update.callback_query
    data = query.data
    current_text_i = update.effective_message.text.replace('\nБот: В этом месте вы можите узнать погоду', '')
    if current_text_i.lower() == 'привет':
        current_text_i = 'Hello city'
    current_text_replace = current_text_i.replace('\n Бот: Что вам именно нужно узнать?', '')
    if data == 'WEATHER':
        query.edit_message_text(
            text=current_text_i + '\n Бот: Что вам именно нужно узнать?\n',
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=weather_list()
                               )
    elif data == 'STATUS':
        query.edit_message_text(
            text=Geocoder.weather_stats(current_text_replace),
            parse_mode=ParseMode.MARKDOWN,
        )
    elif data == 'TEMPERATURE':
        query.edit_message_text(
            text=Geocoder.weather_temperature(current_text_replace),
            parse_mode=ParseMode.MARKDOWN,
        )
    elif data == 'SPEED_WIND':
        query.edit_message_text(
            text=Geocoder.weather_wind(current_text_replace),
            parse_mode=ParseMode.MARKDOWN,
        )
    elif data == 'NOTHING':
        query.edit_message_text(
            text='Что тогда?',
            parse_mode=ParseMode.MARKDOWN,
        )
    elif data == 'GEOLOCATION':
        query.edit_message_text(
            text='Бот: Вот где это находится\n' + current_text_replace + ' ' + Geocoder.geo(current_text_replace),
            parse_mode=ParseMode.MARKDOWN
        )