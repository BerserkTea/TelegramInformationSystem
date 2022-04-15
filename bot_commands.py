from turtle import up
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *



def greeting_command(update: Update, context: CallbackContext):  #прописать потом условие, что, если участник вновь прибывший, то привествие и знакомство другое
    log(update,context)
    update.message.reply_text(f'Oh my dear {update.effective_user.first_name}')
    update.message.reply_text(f"Let's talk")
    update.message.reply_text(f'Make your choice:\n/time - time right now\n/help - see all functions\n/sum - write two numbers with whitespace')

"""" if user_id not in contacts.txt:
        update.message.reply_text(f'Nice to meet you {update.effective_user.first_name}')
        update.message.reply_text(f"/About you - Tell us some words about you?")
        update.message.reply_text(f"/About our group - !!!!!!!!!Напишу текст")
"""





def help_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'/start\n/time\n/help\n/sum')

def time_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')
    
def sum_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Введите два числа через пробел:')
    msg = update.message.text
    items = msg.split()
    num1 = int(items[1])
    num2 = int(items[2])
    update.message.reply_text(f'{num1} + {num2} = {num1+num2}')

def get_text_message (update: Update, context: CallbackContext):
    if update.message.text == "/start":
        update.message.reply_text(f'i know that i know nothing')
    else:
          update.message.reply_text(f'right choice') 

