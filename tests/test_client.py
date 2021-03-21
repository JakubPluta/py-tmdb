import pytest
from tmdb.client import TMDBClient


def test_client_properly_instantiate():
    client_instance = TMDBClient()

    assert client_instance.base_url == 'https://api.themoviedb.org/3'
    assert client_instance._session.params['api_key'] is not None


