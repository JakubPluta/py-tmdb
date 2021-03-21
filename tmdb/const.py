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

GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"

ENDPOINTS = {
    "ACCOUNT": {
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
        "mark_as_favorite": "/account/{account_id}/favorite",  # Mark a movie or TV show as a favorite item
        "add_to_watchlist" : "/account/{account_id}/watchlist"   # Add a movie or TV show to your watchlist.
    },

    "MOVIES": {
        # GET METHODS
        'details': '/movie/{movie_id}',  # Get the primary information about a movie
        'account_states': '/movie/{movie_id}/account_states',  # Grab Movie rating,
        'alternative_titles': '/movie/{movie_id}/alternative_titles',  # Get all of the alternative titles for a movie
        'changes': '/movie/{movie_id}/changes',  # Get the changes for a movie. By default only the last 24 hours
        'credits': '/movie/{movie_id}/credits',  # Get the cast and crew for a movie.
        'external_ids': '/movie/{movie_id}/external_ids',  # Get the external ids for a movie
        'images': '/movie/{movie_id}/images',  # Get the images that belong to a movie.
        'keywords': '/movie/{movie_id}/keywords',  # Get the keywords that have been added to a movie.
        "release_date": "/movie/{movie_id}/release_dates",  # Get the release dates
        'videos': '/movie/{movie_id}/videos',  # Get the videos that have been added to a movie.
        'translations': '/movie/{movie_id}/translations',  # Get a list of translations created for a movie.
        'recommendations': '/movie/{movie_id}/recommendations',  # Get a list of recommended movies for a movie.
        'similar_movies': '/movie/{movie_id}/similar_movies',  # Get a list of similar movies
        'reviews': '/movie/{movie_id}/reviews',  # Get the user reviews for a movie.
        'lists': '/movie/{movie_id}/lists',  # Get a list of lists that this movie belongs to.
        'latest': '/movie/latest',  # Get the most newly created movie. This is a live response
        'now_playing': '/movie/now_playing',  # Get a list of movies in theatres.
        'popular': '/movie/popular',  # Get a list of the current popular movies on TMDb.
        'top_rated': '/movie/top_rated',  # Get the top rated movies on TMDb.
        'upcoming': '/movie/upcoming',  # Get a list of upcoming movies in theatres.
        'watch_providers': '/movie/{movie_id}/watch/providers',  # Get a list of the availabilities per country


        # POST METHODS
        'rating': '/movie/{id}/rating',  # Rate a movie

        # DELETE METHODS
        'rating_delete': '/movie/{id}/rating',  # Remove your rating for a movie.
    }
}