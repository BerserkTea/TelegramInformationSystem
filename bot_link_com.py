from ntpath import join
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from spy import *
from random import choice
import csv
# 
def link_command(update: Update, context: CallbackContext):
    log(update,context)
    with open ('usefull_link.csv', newline='', encoding='UTF-8') as us_link:
        csv_link=list(csv.reader(us_link)) 
        update.message.reply_text(f'{choice(csv_link)}')