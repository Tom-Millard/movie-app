from requests import get
from requests.exceptions import RequestException
from movie.MovieDetails import MovieDetails
import json
from typing import Union
import os


def get_movie(movie_id: str) -> Union[None, MovieDetails]:
    key = os.getenv('OMDB_KEY')
    url = 'http://www.omdbapi.com/?apikey={}&i={}&plot=full'.format(key,movie_id)
    raw_json: json = __request_json(url)
    movie: dict = raw_json

    if 'Response' in movie and str(movie['Response']) == 'True':
        return MovieDetails(movie_id, raw_json)

    return None


def __request_json(url: str) -> dict:
    content = get(url)

    if content.status_code is not 200:
        raise RequestException('response was not 200 - {}'.format(content.status_code))

    return json.loads(content.content)
