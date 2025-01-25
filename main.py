from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import os

votes = {
    "likes": 0, 
    "dislikes": 0
    }

TOKEN = os.getenv("TOKEN")

def start(update, context):

    photo =f"https://minapi.beemarket.uz/prod-media/productImages/thumbnails/medium/1726834437OHIFEMxr0Z6k.webp"

    keyboard = [
        [InlineKeyboardButton(f"👍 Like {votes['likes']}", callback_data="like")],
        [InlineKeyboardButton(f"👎  Dislike {votes['dislikes']}", callback_data="dislike")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_photo(photo=photo, reply_markup=reply_markup)
    



updater = Updater(TOKEN)  
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))


updater.start_polling()
updater.idle()
