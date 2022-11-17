import telebot
from Token import TOKEN
from MATH import *
from telebot import types
from logg import Logg

bot = telebot.TeleBot(TOKEN())
global text, text2
text = text2 = 0


def proverka(call, n):
    if n > 0:
        bot.send_message(call.message.chat.id, 'Введи числа через пробел')
    else:
        bot.send_message(
            call.message.chat.id, "Введи числа через пробел пример: 1+2j 3-10j ... -n+nj: ")


def operations(message, num):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton("Сумма", callback_data='/sum')
    item2 = types.InlineKeyboardButton("Разница", callback_data='/sub')
    item3 = types.InlineKeyboardButton("Умножение", callback_data='/mult')
    item4 = types.InlineKeyboardButton("Деление", callback_data='/div')
    item5 = types.InlineKeyboardButton("Квадрат", callback_data='/pow')
    item6 = types.InlineKeyboardButton("Корень", callback_data='/sqrt')
    if num > 0:
        markup.add(item, item2, item3, item4)
    else:
        markup.add(item, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, 'Выбери: ', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.row('/starting')
    bot.send_message(
        message.chat.id, 'Привет я бот калькулятор для начала введи /starting', reply_markup=keyboard1)


@bot.message_handler(commands=['starting'])
def start(message):
    global text, text2
    text = text2 = 0
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton(
        "Рациональные числа", callback_data='/rat')
    item2 = types.InlineKeyboardButton(
        "Комплексные числа", callback_data='/com')
    markup.add(item, item2)

    bot.send_message(message.chat.id, 'Выбери: ', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global text, text2
    if call.message:
        if call.data == '/rat':
            text = 1
            operations(call.message, -1)
            Logg(call.message, 'Выбор рациональные числа')

        if call.data == '/com':
            text = -1
            operations(call.message, 1)
            Logg(call.message, 'Выбор комплексные числа')
        if call.data == '/sum':
            text2 = 1
            proverka(call, text)
            Logg(call.message, 'Выбор сумма')
        elif call.data == '/sub':
            text2 = 2
            proverka(call, text)
            Logg(call.message, 'Выбор разница')
        elif call.data == '/mult':
            text2 = 3
            proverka(call, text)
            Logg(call.message, 'Выбор умножение')
        elif call.data == '/div':
            text2 = 4
            proverka(call, text)
            Logg(call.message, 'Выбор деление')
        elif call.data == '/pow':
            text2 = 5
            proverka(call, text)
            Logg(call.message, 'Выбор квадрат')
        elif call.data == '/sqrt':
            text2 = 6
            proverka(call, text)
            Logg(call.message, 'Выбор корень')


@bot.message_handler(content_types=['text'])
def send_text(message):
    global text, text2
    Logg(message, message.text)
    if message.text.replace("-", "").replace(".", "").replace(" ", "").replace("j", '').replace("+", "").isdigit():
        x = message.text

        if text == 1 and message.text.replace("-", "").replace(".", "").replace(" ", "").isdigit():

            if text2 == 1:
                bot.send_message(
                    message.chat.id, f'Ответ: {sum(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {sum(x, text)}')
            elif text2 == 2:
                bot.send_message(
                    message.chat.id, f'Ответ: {sub(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {sub(x, text)}')
            elif text2 == 3:
                bot.send_message(
                    message.chat.id, f'Ответ: {mult(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {mult(x, text)}')
            elif text2 == 4:
                bot.send_message(
                    message.chat.id, f'Ответ: {div(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {div(x, text)}')
            elif text2 == 5:
                bot.send_message(
                    message.chat.id, f'Ответ: {pow(x)}', parse_mode='html')
                Logg(message, f'Ответ {pow(x)}')
            elif text2 == 6:
                bot.send_message(
                    message.chat.id, f'Ответ: {sqrt(x)}', parse_mode='html')
                Logg(message, f'Ответ {sqrt(x)}')
            else:
                bot.send_message(
                    message.chat.id, "ERROR вы ввели не число или совершили ошибку", parse_mode='html')
                Logg(message, "ERROR вы ввели не число или совершили ошибку")

        elif text == -1:
            if text2 == 1:
                bot.send_message(
                    message.chat.id, f'Ответ: {sum(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {sum(x, text)}')
            elif text2 == 2:
                bot.send_message(
                    message.chat.id, f'Ответ: {sub(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {sub(x, text)}')
            elif text2 == 3:
                bot.send_message(
                    message.chat.id, f'Ответ: {mult(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {mult(x, text)}')
            elif text2 == 4:
                bot.send_message(
                    message.chat.id, f'Ответ: {div(x,text)}', parse_mode='html')
                Logg(message, f'Ответ {div(x, text)}')
    else:

        if message.text.lower() == 'саня гей?' or message.text.lower() == 'саня гей':
            bot.send_message(
                message.chat.id, "Да саня определенно гей!!!", parse_mode='html')
        else:
            bot.send_message(
                message.chat.id, "ERROR вы ввели не число или совершили ошибку", parse_mode='html')


bot.polling()
