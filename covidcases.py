import arrow
import requests
from dateutil import tz
from datetime import datetime


def humanize_date(any_date):
    return arrow.get(any_date).replace(tzinfo='+05:45').humanize()


def get_today_updates(update, context):
    improved = {}
    updates = requests.get(
        'https://covid19.mohp.gov.np/covid/api/confirmedcases').json()["nepal"]
    improved.update({
        'tested': updates['today_pcr'],
        'positive': updates['today_newcase'],
        'recovered': updates['today_recovered'],
        'deaths': updates['today_death'],
        'updated': humanize_date(updates['updated_at'])
    })
    update.message.reply_text(improved)


def get_local_updates(update, context):
    improved = {}
    updates = requests.get(
        'https://covid19.mohp.gov.np/covid/api/confirmedcases').json()["nepal"]
    improved.update({
        'tested': updates['samples_tested'],
        'positive': updates['positive'],
        'recovered': updates['extra1'],
        'deaths': updates['deaths'],
        'updated': humanize_date(updates['updated_at'])
    })
    update.message.reply_text(improved)


def get_world_updates(update, context):
    improved = {}
    updates = requests.get(
        'https://data.nepalcorona.info/api/v1/world').json()
    improved.update({
        'tested': updates['tests'],
        'positive': updates['cases'],
        'recovered': updates['recovered'],
        'deaths': updates['deaths'],
        'updated': humanize_date(datetime.fromtimestamp(int(updates['updated']/1000)))
    })
    update.message.reply_text(improved)


def get_website(update, context):
    update.message.reply_text("https://covidnepal.now.sh")


def get_about(update, context):
    about = f'''Telegram bot that provides you detailed look at COVID-19 cases inside Nepal.
Web version lives at: https://covidnepal.now.sh
    
Version: 1.2.0   
Made by sidbelbase.'''
    update.message.reply_text(about)
