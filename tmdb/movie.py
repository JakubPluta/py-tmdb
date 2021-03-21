from tmdb.client import TMDBClient
from tmdb.const import ENDPOINTS


class Movies(TMDBClient):

    BASE = 'MOVIES'
    ENDPOINT_URLS = ENDPOINTS[BASE]

    def __init__(self, movie_id: int = 0):
        super(Movies, self).__init__()
        self.movie_id = movie_id

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
        """Grab the following account states for a session:
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
        """Get all of the alternative titles for a movie.

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
        """Get the changes for a movie. By default only the last 24 hours are returned.
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
