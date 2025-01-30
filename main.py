from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from tinydb import TinyDB, Query
db=TinyDB('db.json',indent=4)
import os

votes = {
    "likes": 0, 
    "dislikes": 0,
    "smile": 0,
    "laugh": 0,
    "angry": 0,
    }

TOKEN = os.getenv("TOKEN")

def start(update, context):

    photo =f"https://minapi.beemarket.uz/prod-media/productImages/thumbnails/medium/1726834437OHIFEMxr0Z6k.webp"

    keyboard = [
        [InlineKeyboardButton(f"👍 Like {votes['likes']}", callback_data="like")],
        [InlineKeyboardButton(f"👎  Dislike {votes['dislikes']}", callback_data="dislike")],
        [InlineKeyboardButton(f"😊  Laugh {votes['laugh']}", callback_data="laugh")],
        [InlineKeyboardButton(f"😂  Smile {votes['smile']}", callback_data="smile")],
        [InlineKeyboardButton(f"😡  Angry {votes['angry']}", callback_data="angry")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_photo(photo=photo, reply_markup=reply_markup)
    

def like(update, context):
    q=Query()
    if update.callback_query.data == "like":
        votes["likes"] += 1
        db.insert({"likes": votes["likes"],"username": update.callback_query.from_user.username,"chat_id": update.callback_query.message.chat_id})
    elif update.callback_query.data == "dislike":
        votes["dislikes"] += 1
        db.insert({"dislikes": votes["dislikes"],"username": update.callback_query.from_user.username,"chat_id": update.callback_query.message.chat_id})
    elif update.callback_query.data == "laugh":
        votes["laugh"] += 1
        db.insert({"laugh": votes["laugh"],"username": update.callback_query.from_user.username,"chat_id": update.callback_query.message.chat_id})
    elif update.callback_query.data == "smile":
        votes["smile"] += 1
        db.insert({"smile": votes["smile"],"username": update.callback_query.from_user.username,"chat_id": update.callback_query.message.chat_id})
    elif update.callback_query.data == "angry":
        votes["angry"] += 1
        db.insert({"angry": votes["angry"],"username": update.callback_query.from_user.username,"chat_id": update.callback_query.message.chat_id})
    keyboard = [
        [InlineKeyboardButton(f"👍 Like {votes['likes']}", callback_data="like")],
        [InlineKeyboardButton(f"👎 Dislike {votes['dislikes']}", callback_data="dislike")],
        [InlineKeyboardButton(f"😊 Laugh {votes['laugh']}", callback_data="laugh")],
        [InlineKeyboardButton(f"😂 Smile {votes['smile']}", callback_data="smile")],
        [InlineKeyboardButton(f"😡 Angry {votes['angry']}", callback_data="angry")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_reply_markup(reply_markup=reply_markup) 

    

updater = Updater(TOKEN)  
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(like))

updater.start_polling()
updater.idle()
