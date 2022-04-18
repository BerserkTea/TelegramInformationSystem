from distutils import command
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
from bot_link_com import *

updater = Updater('5334748744:AAGZuS8H575cbDURtkt6qX9eRHGiUGB8yMA')

updater.dispatcher.add_handler(CommandHandler('start', greeting_command))   
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum',sum_command))
updater.dispatcher.add_handler(CommandHandler('link',link_command))
updater.dispatcher.add_handler(CommandHandler('memes', photo_command))


print("server starts")
updater.start_polling()
updater.idle()
