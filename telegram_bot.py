
import telegram
from telegram.ext import Updater, MessageHandler, Filters
import re
from main import parse_trendyol_product

bot = telegram.Bot(token='6681043404:AAEL0YLg_mj2QmJ_kK08mZUmS8vFbDOJSPw')

def parse_trendyol_link(link):
    images = parse_trendyol_product(link)
    return images

def handle_message(update, context):
    message = update.message.text
    if re.match(r'^https://www.trendyol.com/', message):
        images = parse_trendyol_link(message)
        for image in images:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=image)

updater = Updater(token='6681043404:AAEL0YLg_mj2QmJ_kK08mZUmS8vFbDOJSPw', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
updater.idle()