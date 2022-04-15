# TelegramInformationSystem
python3 -m venv .folder
далее нажимаем F1
пишем Python:Select interpreter
    выбираем строку содержащую .folder venv
    далее запускаем новый терминал
    пишем cd .\.folder\Scripts\
    и пишем .\Activate.ps1
    после этого должна появиться вначале строки консоли приставка ((.folder) ) это и будет означать что вы работаете в виртуальной среде к кнокретному проекту. в ней выполняем:
        pip install python-telegram-bot
            '''         from telegram import Update
                        from telegram.ext import Updater, CommandHandler, CallbackContext
                        def hello(update: Update, context: CallbackContext) -> None:
                            update.message.reply_text(f'Hello {update.effective_user.first_name}')

                        updater = Updater('YOUR TOKEN HERE')

                        updater.dispatcher.add_handler(CommandHandler('hello', hello))

                        updater.start_polling()
                        updater.idle()) '''