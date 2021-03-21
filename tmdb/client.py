import json
import requests
from . import SESSION
from .const import BASE_URL, API_VERSION


class TMDBClient:
    ENDPOINT_BASE = None
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

