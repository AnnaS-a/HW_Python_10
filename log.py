from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext, text):
    file = open('C:\\Users\\Sluki\\Desktop\\GB\\VSC_Python\\Seminars\\S10_2\\res.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {text}\n')
    file.close()
