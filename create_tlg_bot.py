from distutils import command
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5331187324:AAGU7esB7TQvG3r8i8B963HaPFPW7U-v52I')

updater.dispatcher.add_handler(CommandHandler('start', greeting_command))   
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum',sum_command))



print("server starts")
updater.start_polling()
updater.idle()
