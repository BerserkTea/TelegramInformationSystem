from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime

def log(update: Update, context: CallbackContext):
    file = open ('db.csv','a', encoding='UTF-8')
    file.write (f'{datetime.now()}:{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()
