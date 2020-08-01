import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from covidcases import get_about, get_website, get_local_updates, get_today_updates, get_world_updates, get_province_updates
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
dotenvsecrets = os.path.join(basedir, '.env')
load_dotenv(dotenvsecrets)

TOKEN = os.environ.get('TOKEN')
NAME = "covidnepalbot"
HOST = "0.0.0.0"
PORT = 5000

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def province_chooser(update, context):
    keyboard = [[InlineKeyboardButton("Province 1", callback_data='1'),
                 InlineKeyboardButton("Province 2", callback_data='2')],
                [InlineKeyboardButton("Bagmati Province", callback_data='3'),
                 InlineKeyboardButton("Gandaki Province", callback_data='4')],
                [InlineKeyboardButton("Province 5", callback_data='5'),
                 InlineKeyboardButton("Karnali Province", callback_data='6')],
                [InlineKeyboardButton("Sudurpaschim Province", callback_data='7')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Please choose a province to see updates:', reply_markup=reply_markup)


def send_province(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(get_province_updates(query.data))


def send_help(update, context):
    help_commands = f'''Type the following commands to get started:

/updates - Get local updates
/provinces - Get province updates
/today - Get today's updates
/worldwide - Get worldwide updates
/about - About this bot
/help - To get help messages
/website - Go to website

covidnepal_bot • Version 1.2.3
    '''
    update.message.reply_text(help_commands)


def start(update, context):
    user = update.message.from_user.first_name
    help_commands = f'''Hello {user}, Welcome to covidnepal.

Please type the following commands to get started:

/updates - Get local updates
/provinces - Get province updates
/today - Get today's updates
/worldwide - Get worldwide updates
/about - About this bot
/help - To get help messages
/website - Go to website

covidnepal_bot • Version 1.2.3
    '''
    update.message.reply_text(help_commands)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_error_handler(error)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", send_help))
    dp.add_handler(CallbackQueryHandler(send_province))
    dp.add_handler(CommandHandler("about", get_about))
    dp.add_handler(CommandHandler("website", get_website))
    dp.add_handler(CommandHandler("today", get_today_updates))
    dp.add_handler(CommandHandler("updates", get_local_updates))
    dp.add_handler(CommandHandler("provinces", province_chooser))
    dp.add_handler(CommandHandler("worldwide", get_world_updates))

    updater.start_webhook(listen=HOST, port=PORT, url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    # updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
