import arrow
import requests
from dateutil import tz
from datetime import datetime


def humanize_date(any_date):
    return arrow.get(any_date).humanize()


def get_today_updates(update, context):
    updates = requests.get(
        'https://covid19.mohp.gov.np/covid/api/confirmedcases').json()["nepal"]
    improved = f'''Today's Covid Updates:

Tested : {updates['today_pcr']}
Positive : {updates['today_newcase']}
Recovered : {updates['today_recovered']}
Deaths : {updates['today_death']}

Updated  {humanize_date(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_local_updates(update, context):
    updates = requests.get(
        'https://covid19.mohp.gov.np/covid/api/confirmedcases').json()["nepal"]

    improved = f'''Nepali Covid Updates:

Tested : {updates['samples_tested']}
Positive : {updates['positive']}
Recovered : {updates['extra1']}
Deaths : {updates['deaths']}

Updated {humanize_date(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_world_updates(update, context):
    updates = requests.get(
        'https://data.nepalcorona.info/api/v1/world').json()
    improved = f'''Worldwide Covid Updates:

Tested : {updates['tests']}
Positive : {updates['cases']}
Recovered : {updates['recovered']}
Deaths : {updates['deaths']}

Updated {humanize_date(datetime.fromtimestamp(int(updates['updated']/1000)))}
'''
    update.message.reply_text(improved)


def get_website(update, context):
    update.message.reply_text("https://covidnepal.now.sh")


def get_about(update, context):
    about = f'''Telegram bot that provides you detailed look at COVID-19 cases inside Nepal.
Web version lives at: https://covidnepal.now.sh
    
Version: 1.2.0   
Made by sidbelbase.'''
    update.message.reply_text(about)
