import telebot
from Token import TOKEN
from MATH import *

bot = telebot.TeleBot(TOKEN())
NUMBERS = 0
def MATH(n):
    if NUMBERS == 1:
        sum(n)
    elif NUMBERS == 2:
        sub(n)
    elif NUMBERS == 3:
        mulf(n)
    elif NUMBERS == 4:
        div(n)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Рад видить вас {message.from_user.first_name} {message.from_user.last_name}\nЯ бот калькулятор узнать больше /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    mess = 'Я бот калькулятор могу посчитать \nСумма введите /sum' \
           '\nРазница введите /sub\nУмножение /mult\nДеление /div'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['sum'])
def start_Sum(message):
    global NUMBERS
    NUMBERS = 1
    bot.send_message(message.chat.id,'Введите число', parse_mode='html')
@bot.message_handler(commands=['sub'])
def start(message):
    global NUMBERS
    NUMBERS = 2
    bot.send_message(message.chat.id, 'Введите число', parse_mode='html')
@bot.message_handler(commands=['div'])
def start(message):
    global NUMBERS
    NUMBERS = 3
    bot.send_message(message.chat.id, 'Введите число', parse_mode='html')
@bot.message_handler(commands=['sum'])
def start(message):
    bot.send_message(message.chat.id, 'Введите числа ', parse_mode='html')
    n = message.text
    if n.replace("-", "").replace(".", "").replace(" ", "").isdigit():
        bot.send_message(message.chat.id, sum(n), parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'ERROR ввели не число', parse_mode='html')





bot.polling(none_stop=True)
