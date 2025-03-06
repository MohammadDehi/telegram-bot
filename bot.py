from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

TOKEN = "7323889209:AAHTEba0jo8ryl3y7SkBZY-tst_s2JlSE48"
ADMIN_ID = 5763139251

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! پیام خود را ارسال کنید.")

def forward_to_admin(update: Update, context: CallbackContext) -> None:
    context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_admin))

updater.start_polling()
updater.idle()
