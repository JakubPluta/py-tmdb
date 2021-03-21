import json
import requests
from . import SESSION, HEADERS, API_KEY
from .const import BASE_URL, API_VERSION, GET, POST, PUT, DELETE


class SessionFactory:
    @classmethod
    def create_session(cls):
        session = requests.Session()
        session.headers = HEADERS
        session.params['api_key'] = API_KEY
        return session


class TMDBClient:

    _ENDPOINT = None
    ENDPOINT_URLS = {}

    def __init__(self, session: requests.Session = SESSION):
        self._session = session
        self._api_version = API_VERSION
        self._base_url = BASE_URL + self._api_version

    @property
    def version(self):
        return self._api_version

    @version.setter
    def version(self, version: [str, int]):
        if isinstance(str, version):
            self._api_version = version
        else:
            self._api_version = str(version)

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, url: str):
        self._base_url = url

    @property
    def parameters(self):
        if self._session and self._session.params is not None:
            return self._session.params

    def _build_url_path(self, endpoint):
        return f"{self._base_url}{self.ENDPOINT_URLS[endpoint]}"

    def _get_movie_id_path(self, endpoint):
        return self._build_url_path(endpoint).format(movie_id=self.movie_id)

    def _make_request(self, method, url, params: dict = None, data: dict = None, resp_json=True):
        data = json.dumps(data) if data else data

        if not self._session:
            self._session = SessionFactory.create_session()

        response = self._session.request(method, url, params, data)
        response.raise_for_status()
        if resp_json:
            return response.json()
        else:
            return response.content

    def _get_method(self, endpoint, params):
        return self._make_request(GET, endpoint, params)

    def _post_method(self, endpoint, params, data):
        return self._make_request(POST, endpoint, params, data)

    def _delete_method(self, endpoint, params, data):
        return self._make_request(DELETE, endpoint, params, data)

    def _put_method(self, endpoint, params, data):
        return self._make_request(PUT, endpoint, params, data)
