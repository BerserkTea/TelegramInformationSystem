from turtle import up
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from TelegramInformationSystem.spy import *



def greeting_command(update: Update, context: CallbackContext):
    log(update,context)
    update.message.reply_text(f'Oh my dear {update.effective_user.first_name}')
    update.message.reply_text(f'Make your choice:\n/time - time right now\n/help - see all functions\n/sum - write two numbers with whitespace')

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

def get_message (update: Update, context: CallbackContext):
    msg = update.message.text
    if msg != 'start' or 'help' or 'sum' or 'time':
        update.message.reply_text(f'i know that i know nothing')
    else:
          update.message.reply_text(f'right choice') 

