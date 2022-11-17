import telebot
from telebot import types
from models import *
from random import randint
import sqlite3
import xlsxwriter
from sqlalchemy.sql import text

token = '5770384309:AAGfLGofyPfvFKyhFemQFF_lJV_T5km0IW0'
bot = telebot.TeleBot(token)

markup = types.InlineKeyboardMarkup(row_width=1)
start_button = types.InlineKeyboardButton("Записать работника", callback_data='start')
markup.add(start_button)


@bot.message_handler(commands=['start'])
def start_commands(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Вы в главном меню', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "start":
        bot.send_message(call.message.chat.id, 'Введите ФИО работника')
        bot.register_next_step_handler(call.message, registration)


def registration(message):
    name = message.text
    with engine.connect() as conn:
        conn.execute(insert(text('users'), ["fio", "datar", "id_role"]).values({"fio": name, "datar": '11.08.1984', "id_role": randint(1, 2)}))
        conn.commit()
    workbook = xlsxwriter.Workbook('users.xlsx')
    worksheet = workbook.add_worksheet()
    fio = 'SELECT fio FROM users'
    datar = 'SELECT datar FROM users'
    role = 'SELECT r.name AS name FROM roles AS r LEFT JOIN users AS u ON r.id = u.role_id'
    expenses = (
        ['ФИО', fio],
        ['Дата рождения', datar],
        ['Наименование роли', role],
    )

    row = 0
    col = 0

    for item, cost in (expenses):
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost)
        row += 1
    workbook.close()
    f = open('users.xlsx', 'rb')
    bot.send_document(message.chat.id, f)
    bot.register_next_step_handler(message, start_commands)


bot.polling(none_stop=True, interval=0)