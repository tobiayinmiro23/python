from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_URL = "/prod/v1/today.json"
url = "https://api.unsplash.com/photos/?client_id=3ALI7oiWjQD3B2aqBzlqsJL64T_-9qsknDF6KWFYoEU&page=1&per_page=12"
printer = PrettyPrinter()
response = get(url).json()
printer.pprint(response)
