basedir = os.path.abspath(os.path.dirname(__file__))
dotenvsecrets = os.path.join(basedir, '.env')
load_dotenv(dotenvsecrets)

HOST = "0.0.0.0"
TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
MY_WEBSITE = "https://sarojbelbase.com.np"
API_URL = "https://api.sarojbelbase.com.np"
BHUNTE_API_URL = "https://data.askbhunte.com/api/v1"
WEBHOOK_URL = f"https://covidbot.sarojbelbase.com.np/{TOKEN}"
MOHP_API_URL = "https://covid19.mohp.gov.np/covid/api/confirmedcases"