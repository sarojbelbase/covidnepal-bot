import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, Updater

from covidcases import (get_about, get_local_updates, get_province_updates,
                        get_today_updates, get_website, get_world_updates)
from const import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def province_chooser(update, context):
    keyboard = [[InlineKeyboardButton("Province 1", callback_data='1'),
                 InlineKeyboardButton("Province 2", callback_data='2')],
                [InlineKeyboardButton("Bagmati Province", callback_data='3'),
                 InlineKeyboardButton("Gandaki Province", callback_data='4')],
                [InlineKeyboardButton("Lumbini Province", callback_data='5'),
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
    help_commands = f'''Type or click the following commands to get started:

/updates - Get whole nepal updates
/provinces - Get province updates
/today - Get today's updates
/worldwide - Get global updates
/about - About this bot
/help - To get help messages
/website - Go to our official website

covidnepal_bot • Version 2.0.1 • Made by sidbelbase.
'''
    update.message.reply_text(help_commands)


def start(update, context):
    user = update.message.from_user.first_name
    help_commands = f'''Hello {user}, Welcome to covidnepal_bot.

Type or click the following commands to get started:

/updates - Get whole nepal updates
/provinces - Get province updates
/today - Get today's updates
/worldwide - Get global updates
/about - About this bot
/help - To get help messages
/website - Go to our official website

covidnepal_bot • Version 2.0.1 • Made by sidbelbase.
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

    updater.start_webhook(
        listen=HOST,
        port=PORT,
        url_path=TOKEN,
        webhook_url=WEBHOOK_URL
    )

    # updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
