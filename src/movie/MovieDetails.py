import json
import re
import datetime


class MovieDetails:

    __movie_id = str
    __details = json
    __releaseDate = {}

    def __init__(self, movie_id: str, details: json):

        if bool(re.match('^tt', movie_id)) is False:
            raise ValueError('Movie id is not a valid movie id: {}'.format(movie_id))

        self.__movie_id = movie_id
        self.__details = details

    def movie_id(self) -> str:
        return self.__movie_id

    def details(self) -> json:
        return self.__details
    
    def addReleaseDate(self, iso: str, release_date: datetime) -> None:
      self.__releaseDate[iso] = release_date

    def getReleaseDate(self, country: str) -> datetime:
      return self.__releaseDate.get(country)