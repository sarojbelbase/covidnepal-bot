import requests
from datetime import datetime
from const import *
from utils import padding, humanize_date, humanize_local_date


def get_province_updates(province_id):
    url = f"{API_URL}/api/v1/covid/province/{int(province_id)}"
    province = requests.get(url).json()
    improved = f'''{province["name"]}'s Covid Updates:

Tested : {padding(province["tested"])}
Positive : {padding(province["cases"])}
Recovered : {padding(province["recovered"])}
Deaths : {padding(province["deaths"])}

Updated {humanize_date(province["last_updated"])} 
    '''
    return improved


def get_today_updates(update, context):
    url = f'{API_URL}/api/v1/covid/today/generate'
    updates = requests.get(url)
    update.message.reply_photo(updates.content)


def get_local_updates(update, context):
    updates = requests.get(MOHP_API_URL).json()["nepal"]
    improved = f'''Nepal's Covid Updates:

Tested : {padding(updates['samples_tested'])}
Positive : {padding(updates['positive'])}
Recovered : {padding(updates['extra1'])}
Deaths : {padding(updates['deaths'])}

Updated {humanize_local_date(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_world_updates(update, context):
    url = f'{BHUNTE_API_URL}/world'
    updates = requests.get(url).json()
    improved = f'''Worldwide Covid Updates:

Tested : {padding(updates['tests'])}
Positive : {padding(updates['cases'])}
Recovered : {padding(updates['recovered'])}
Deaths : {padding(updates['deaths'])}

Updated {humanize_date(datetime.utcfromtimestamp(int(updates['updated']/1000)))}
'''
    update.message.reply_text(improved)


def get_website(update, context):
    update.message.reply_text(MY_WEBSITE)


def get_about(update, context):
    about = f'''Telegram bot that provides you detailed look at COVID-19 cases inside Nepal.
Web version is available at: https://covid.sarojbelbase.com.np
    
Version: 2.0.1 • Made by sidbelbase.'''
    update.message.reply_text(about)
