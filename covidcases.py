import arrow
import requests
from dateutil import tz
from datetime import datetime, timezone


def padding(any_num):
    if int(any_num) < 10:
        return '0' + str(any_num)
    else:
        return f"{int(any_num):,}"


def humanize_date(any_date):
    return arrow.get(any_date).replace(tzinfo=timezone.utc).humanize()


def humanize_nonutc(any_date):
    return arrow.get(any_date).humanize()


def get_province_updates(province_id):
    province = requests.get(
        f"https://covidapi.mohp.gov.np/api/v1/stats/?province={int(province_id)}"
    ).json()
    province = province[0]
    improved = f'''{province["province_name"]}'s Covid Updates:

Tested : {padding(province["total_tested"])}
Positive : {padding(province["total_positive"])}
Recovered : {padding(province["total_recovered"])}
Deaths : {padding(province["total_death"])}

Updated {humanize_date(province["update_date"])} 
    '''
    return improved


def get_today_updates(update, context):
    updates = requests.get(
        'https://covid19.mohp.gov.np/covid/api/confirmedcases').json()["nepal"]
    improved = f'''Today's Covid Updates:

Tested : {padding(updates['today_pcr'])}
Positive : {padding(updates['today_newcase'])}
Recovered : {padding(updates['today_recovered'])}
Deaths : {padding(updates['today_death'])}

Updated {humanize_nonutc(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_local_updates(update, context):
    updates = requests.get(
        'https://covid19.mohp.gov.np/covid/api/confirmedcases').json()["nepal"]

    improved = f'''Nepal's Covid Updates:

Tested : {padding(updates['samples_tested'])}
Positive : {padding(updates['positive'])}
Recovered : {padding(updates['extra1'])}
Deaths : {padding(updates['deaths'])}

Updated {humanize_nonutc(updates['updated_at'])}
'''
    update.message.reply_text(improved)


def get_world_updates(update, context):
    updates = requests.get(
        'https://data.nepalcorona.info/api/v1/world').json()
    improved = f'''Worldwide Covid Updates:

Tested : {padding(updates['tests'])}
Positive : {padding(updates['cases'])}
Recovered : {padding(updates['recovered'])}
Deaths : {padding(updates['deaths'])}

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
