import requests
from datetime import datetime
from utils import padding, humanize_date, humanize_local_date


def get_province_updates(province_id):
    url = f"https://api.sarojbelbase.com.np/api/v1/covid/province/{int(province_id)}"
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
    url = 'https://api.sarojbelbase.com.np/api/v1/covid/today/generate'
    updates = requests.get(url)
    update.message.reply_photo(updates.content)


def get_local_updates(update, context):
    url = 'https://covid19.mohp.gov.np/covid/api/confirmedcases'
    updates = requests.get(url).json()["nepal"]
    improved = f'''Nepal's Covid Updates:

Tested : {padding(updates['samples_tested'])}
Positive : {padding(updates['positive'])}
Recovered : {padding(updates['extra1'])}
Deaths : {padding(updates['deaths'])}

Updated {humanize_local_date(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_world_updates(update, context):
    url = 'https://data.askbhunte.com/api/v1/world'
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
    url = "https://covidnepal.sidbelbase.codes"
    update.message.reply_text(url)


def get_about(update, context):
    about = f'''Telegram bot that provides you detailed look at COVID-19 cases inside Nepal.
Web version is available at: https://covidnepal.sidbelbase.codes
    
Version: 2.0.1 • Made by sidbelbase.'''
    update.message.reply_text(about)
