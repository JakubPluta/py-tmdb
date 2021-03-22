from tmdb.client import TMDBClient
from tmdb.const import ENDPOINTS


class Movies(TMDBClient):

    BASE = 'MOVIES'
    ENDPOINT_URLS = ENDPOINTS[BASE]

    def __init__(self, movie_id: int = 0):
        super(Movies, self).__init__()
        self._movie_id = movie_id

    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id: int):
        if isinstance(movie_id, int):
            self._movie_id = movie_id

    def movie_info(self, **kwargs):

        """Get the primary information about a movie.
        Supports append_to_response.

        :param - > as kwargs
            language: [optional]
                description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                type: string
                minLength: 2
                pattern: ([a-z]{2})-([A-Z]{2})
                default: en-US

            append_to_response: [optional]
                description: Append requests within the same namespace to the response.
                type: string
                pattern: ([\w]+)

        :return:
            response:
            Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('details')
        resp = self._get_method(path, kwargs)
        return resp

    def account_states(self, **kwargs):
        """
        Grab the following account states for a session:
            * Movie rating
            * If it belongs to your watchlist
            * If it belongs to your favourite list

            You need to generate a session id. To do that, please visit
            https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id

        :param - > as kwargs
            session_id: [required]
                type: string
            guest_session_id: [optional]
                type: string

        :return:
            response:
            Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('account_states')
        resp = self._get_method(path, kwargs)
        return resp

    def alternative_titles(self, **kwargs):
        """
        Get all of the alternative titles for a movie.

                :param - > as kwargs
                    country: [optional]
                        type: string
                        description: ISO 3166-1 code representing given country
                :return:
                    response:
                    Dictionary from JSON response returned by API
                """

        path = self._get_movie_id_path('alternative_titles')
        resp = self._get_method(path, kwargs)
        return resp

    def changes(self, **kwargs):
        """
        Get the changes for a movie. By default only the last 24 hours are returned.
        You can query up to 14 days in a single query by using the start_date and end_date query parameters.

                :param - > as kwargs
                    start_date: [optional]
                        type: string (format: date)
                        description: Filter the results with a start date.
                    end_date: [optional]
                        type: string (format: date)
                        example: '2016-08-29 16:38:07'
                        description: Filter the results with a end date.
                    page: [optional]
                        type: integer
                        description: Specify which page to query.
                        default: 1
                        min: 1
                        max: 1000

                :return:
                    response:
                    Dictionary from JSON response returned by API
                """

        path = self._get_movie_id_path('changes')
        resp = self._get_method(path, kwargs)
        return resp

    def credits(self, **kwargs):
        """
        Get the cast and crew for a movie.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('credits')
        resp = self._get_method(path, kwargs)
        return resp

    def external_ids(self, **kwargs):
        """
        Get the external ids for a movie. We currently support the following external sources.

            Media Databases	  |   Social IDs
            ---------------------------------
            IMDb ID	Facebook  |  Facebook
                                 Instagram
                                 Twitter

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """
        path = self._get_movie_id_path('external_ids')
        resp = self._get_method(path, kwargs)
        return resp

    def images(self, **kwargs):
        """
        Get the images that belong to a movie.
        Querying images with a language parameter will filter the results.
        If you want to include a fallback language (especially useful for backdrops)
        you can use the include_image_language parameter.
        This should be a comma seperated value like so: include_image_language=en,null.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                include_image_language: [optional]
                    type: string
                    description: This should be a comma seperated value like so: include_image_language=en,null
                    example: en,de
            :return:
                    response:
                    Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('images')
        resp = self._get_method(path, kwargs)
        return resp

    def keywords(self, **kwargs):
        """
        Get the keywords that have been added to a movie.

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('keywords')
        resp = self._get_method(path, kwargs)
        return resp

    def translations(self, **kwargs):
        """
        Get a list of translations that have been created for a movie.

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('translations')
        resp = self._get_method(path, kwargs)
        return resp

    def videos(self, **kwargs):
        """
        Get the videos that have been added to a movie.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('translations')
        resp = self._get_method(path, kwargs)
        return resp

    def watch_providers(self, **kwargs):
        """
        Powered by our partnership with JustWatch,
        you can query this method to get a list of the availabilities per country by provider.
        This is not going to return full deep links, but rather,
        it's just enough information to display what's available where.
        You can link to the provided TMDb URL to help support TMDb and provide the actual deep links to the content.

        Please note: In order to use this data you must attribute the source of the data as JustWatch.
        If we find any usage not complying with these terms we will revoke access to the API.

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """

        path = self._get_movie_id_path('watch_providers')
        resp = self._get_method(path, kwargs)
        return resp

    def lists(self, **kwargs):
        """
        Get a list of lists that this movie belongs to.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                        type: integer
                        description: Specify which page to query.
                        default: 1
                        min: 1
                        max: 1000
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('lists')
        resp = self._get_method(path, kwargs)
        return resp

    def recommendations(self, **kwargs):
        """
        Get a list of recommended movies for a movie.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                        type: integer
                        description: Specify which page to query.
                        default: 1
                        min: 1
                        max: 1000
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('recommendations')
        resp = self._get_method(path, kwargs)
        return resp

    def release_dates(self, **kwargs):
        """
        Get the release date along with the certification for a movie.
        Release dates support different types:
            Premiere
            Theatrical (limited)
            Theatrical
            Digital
            Physical
            TV

            :return:
                    response:
                    Dictionary from JSON response returned by API
        """
        path = self._get_movie_id_path('release_date')
        resp = self._get_method(path, kwargs)
        return resp

    def reviews(self, **kwargs):
        """
        Get the user reviews for a movie.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                        type: integer
                        description: Specify which page to query.
                        default: 1
                        min: 1
                        max: 1000
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('reviews')
        resp = self._get_method(path, kwargs)
        return resp

    def similar_movies(self, **kwargs):
        """
        Get a list of similar movies. This is not the same as the "Recommendation" system you see on the website.
        These items are assembled by looking at keywords and genres.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                        type: integer
                        description: Specify which page to query.
                        default: 1
                        min: 1
                        max: 1000
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('similar')
        resp = self._get_method(path, kwargs)
        return resp

    def rating(self, **kwargs):
        """
        Rate a movie.

        A valid session or guest session ID is required
        "https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id"

        :param - > as kwargs
            session_id: [required]
                type: string
            guest_session_id: [optional]
                type: string
            value: [required]
                description: It will passed in request body:
                example: 8.5
                Request Body: {"value": 8.5}

        :return:
            response:
            Dictionary from JSON response returned by API
        """

        data = dict()
        data['value'] = kwargs.get('value') or None

        path = self._get_movie_id_path('rating')
        resp = self._post_method(path, kwargs, data)

        return resp

    def delete_rating(self, **kwargs):
        """
        Remove your rating for a movie

        A valid session or guest session ID is required
        "https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id"

        :param - > as kwargs
            session_id: [required]
                type: string
            guest_session_id: [optional]
                type: string
            value: [required]
                description: It will passed in request body:
                example: 8.5
                Request Body: {"value": 8.5}

        :return:
            response:
            Dictionary from JSON response returned by API
        """

        data = dict()
        data['value'] = kwargs.get('value') or None

        path = self._get_movie_id_path('rating_delete')
        resp = self._delete_method(path, kwargs, data)

        return resp

    def latest(self, **kwargs):
        """
        Get the most newly created movie.
        This is a live response and will continuously change.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.

            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('latest')
        resp = self._get_method(path, kwargs)
        return resp

    def now_playing(self, **kwargs):
        """
        Get a list of movies in theatres.
        This is a release type query that looks for all movies that have a release type
        of 2 or 3 within the specified date range.

        You can optionally specify a region prameter which will narrow the search to only
        look for theatrical release dates within the specified country.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                    type: integer
                    description: Specify which page to query.
                    default: 1
                    min: 1
                    max: 1000
                region: [optional]
                    type: string
                    description: Specify a ISO 3166-1 code to filter release dates. Must be uppercase.
                    pattern: ^[A-Z]{2}$
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('now_playing')
        resp = self._get_method(path, kwargs)
        return resp

    def popular(self, **kwargs):
        """
        Get a list of the current popular movies on TMDb. This list updates daily.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                    type: integer
                    description: Specify which page to query.
                    default: 1
                    min: 1
                    max: 1000
                region: [optional]
                    type: string
                    description: Specify a ISO 3166-1 code to filter release dates. Must be uppercase.
                    pattern: ^[A-Z]{2}$
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('popular')
        resp = self._get_method(path, kwargs)
        return resp

    def top_rated(self, **kwargs):
        """
        Get the top rated movies on TMDb.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                    type: integer
                    description: Specify which page to query.
                    default: 1
                    min: 1
                    max: 1000
                region: [optional]
                    type: string
                    description: Specify a ISO 3166-1 code to filter release dates. Must be uppercase.
                    pattern: ^[A-Z]{2}$
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('top_rated')
        resp = self._get_method(path, kwargs)
        return resp

    def upcoming(self, **kwargs):
        """
        Get a list of upcoming movies in theatres. This is a release
        type query that looks for all movies that have a release type of 2 or 3 within the specified date range.

        You can optionally specify a region prameter which will narrow the search
        to only look for theatrical release dates within the specified country.

            :param - > as kwargs
                language: [optional]
                    type: string
                    minLength: 2
                    pattern: ([a-z]{2})-([A-Z]{2})
                    default: en-US
                    description: Pass a ISO 639-1 value to display translated data for the fields that support it.
                page: [optional]
                    type: integer
                    description: Specify which page to query.
                    default: 1
                    min: 1
                    max: 1000
                region: [optional]
                    type: string
                    description: Specify a ISO 3166-1 code to filter release dates. Must be uppercase.
                    pattern: ^[A-Z]{2}$
            :return:
                    response:
                    Dictionary from JSON response returned by API
            """

        path = self._get_movie_id_path('upcoming')
        resp = self._get_method(path, kwargs)
        return resp