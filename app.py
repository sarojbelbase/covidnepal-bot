import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from covidcases import get_about, get_website, get_local_updates, get_today_updates, get_world_updates, get_province_updates
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
dotenvsecrets = os.path.join(basedir, '.env')
load_dotenv(dotenvsecrets)

PORT = int(os.environ.get('PORT', 5000))


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TOKEN')


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
/help - help messages
/website - Go to website

covidnepal_bot • Version 1.2.0
    '''
    update.message.reply_text(help_commands)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("website", get_website))
    dp.add_handler(CommandHandler("about", get_about))
    dp.add_handler(CommandHandler("today", get_today_updates))
    dp.add_handler(CommandHandler("updates", get_local_updates))
    dp.add_handler(CommandHandler("worldwide", get_world_updates))
    dp.add_handler(CommandHandler("provinces", province_chooser))
    dp.add_handler(CallbackQueryHandler(send_province))
    dp.add_handler(MessageHandler("help", send_help))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://covidnepal-bot.herokuapp.com/' + TOKEN)
    # updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
