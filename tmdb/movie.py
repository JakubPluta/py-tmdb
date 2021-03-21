from tmdb.client import TMDBClient
from tmdb.const import ENDPOINTS


class Movies(TMDBClient):

    _ENDPOINT = 'MOVIES'
    ENDPOINT_URLS = ENDPOINTS[_ENDPOINT]

    def __init__(self, movie_id: int = 0):
        super(Movies, self).__init__()
        self.movie_id = movie_id

    def movie_info(self, **kwargs):

        """Get the primary information about a movie.
        Supports append_to_response.

        :param - > as a kwargs
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

