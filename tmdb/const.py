COUNTRIES = {
    'EN': 'en-EN',
    'DE': 'de-DE',
    'ES': 'es-ES',
    'FR': 'fr-FR',
    'IN': 'in-IN',
    'IT': 'it-IT',
    "PL": "pl-PL"
}

BASE_URL = "https://api.themoviedb.org/"
API_VERSION = '3'


ENDPOINTS = {
    "Account": {
        "base": '/account',
        "urls": {
            # GET METHODS

            "details": "",  # Get your account details.
            "created_lists": "/{account_id}/lists",  # Get all of the lists created by an account.
            "favorite_movies": "/account/{account_id}/favorite/movies",  # Get the list of your favorite movies.
            "favorite_tv_shows": "/account/{account_id}/favorite/tv",  # Get the list of your favorite TV shows.
            "rated_movies": "/account/{account_id}/rated/movies",  # Get a list of all the movies you have rated.
            "rated_tv_shows": "/account/{account_id}/rated/tv",  # Get a list of all the TV shows you have rated.
            "rated_tv_episodes": "/account/{account_id}/rated/tv/episodes",  # Get TV episodes you have rated.
            "movie_watchlist": "/account/{account_id}/watchlist/movies",  # Movies you have added to your watchlist.
            "tv_watchlist": "/account/{account_id}/watchlist/tv",  # TV shows you have added to your watchlist.

            # POST METHODS
            "mark_as_fav": "/account/{account_id}/favorite",  # Mark a movie or TV show as a favorite item
            "add_to_watchlist" : "/account/{account_id}/watchlist"   # Add a movie or TV show to your watchlist.
        }
    }
}