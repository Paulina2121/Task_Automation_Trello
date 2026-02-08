from datetime import datetime
import os
# Centralized configuration for the project

api_key = os.getenv('API_KEY')
api_token = os.getenv('API_TOKEN')

if not (api_token and api_key):
    raise ValueError("No API token or key found. Check env variables")

QUERY = {
    'key': api_key, #yours api key
    'token': api_token #yours api token
  }
HEADERS = {
    "Accept": "application/json"
  }
HEADERS_ATT = {
    "Authorization": f'OAuth oauth_consumer_key="{QUERY['key']}", oauth_token="{QUERY['token']}"'
}

EXPLICIT_WAIT = 15
PAGE_LOAD_TIMEOUT = 30
BASE_URL = "https://ec.europa.eu/taxation_customs/vies/#/vat-validation"
MAX_RETRIES = 3
URL_FETCH_TASKS = "https://api.trello.com/1/lists/6973b966b66dbb54fde193a6/cards"
BASE_URL_CARDS = "https://api.trello.com/1/cards/"
current_date = datetime.now()
VAT_TASK_NAME = "vat checker"
VAT_FILE_NAME = "vat_numbers_" + current_date.strftime("%Y%m%d_%H%M%S") +".xlsx"
TASK_LIST_FILE = "tasks list.csv"
ID_LIST_DONE = "6973b98b8b19e16988866812"
ID_LIST_EXC = "6973b9931ab4416805aaac69"
ID_LIST_MANUAL = "6973b97c72499cf5c297602d"