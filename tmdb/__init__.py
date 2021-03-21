import os
import requests
from tmdb.exceptions import *

API_KEY = os.environ.get('TMDB', None)



if API_KEY is None:
    raise ApiKeyMissingError(
        "To use api wrapper you are required to register for api key\n"
        "All methods require an API Key\n"
        "To get you API KEY please visit: https://developers.themoviedb.org/3/getting-started/introduction\n"
        "And follow the documentation"
    )


HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'close' # keep-alive
}

SESSION = requests.Session()
SESSION.params['api_key'] = API_KEY
SESSION.params['language'] = "en-EN"
SESSION.headers = HEADERS
