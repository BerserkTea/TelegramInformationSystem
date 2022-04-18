from ctypes import resize
from tracemalloc import start
import telebot
from telebot import types

bot = telebot.TeleBot('5331187324:AAGU7esB7TQvG3r8i8B963HaPFPW7U-v52I')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'"Hello my dear member,{message.from_user.first_name}"')


# @bot.message_handler(commands=['help'])
# def help(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("help", url="https://pypi.org"))
#     bot.send_message(message.chat.id, "you can find smth", reply_markup=markup)


@ bot.message_handler(commands=['menu'])
def menu(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    adress_book=types.KeyboardButton('Look at the adress book')
    mems=types.KeyboardButton('lets have a fun')

    markup.add(adress_book, mems)
    bot.send_message(message.chat.id, "you can choose", reply_markup=markup)


# @bot.message_handler(content_types=["new_chat_members"])
# def handler_new_member(message):
#     user_name = message.new_chat_member.first_name
#     bot.send_message(message.chat.id,"Добро пожаловать в студенческий чат, {0}!".format(user_name))

# bot.message_handler()
print("start")
bot.polling(none_stop=True)
