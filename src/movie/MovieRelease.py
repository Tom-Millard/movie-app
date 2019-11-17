import datetime
import re


class MovieRelease:

    __movie_id = str
    __release_date = datetime
    __country = str

    def __init__(self, movie_id:str, release_date:datetime, country:str):

        if len(movie_id) is 0 or len(country) is 0:
            raise ValueError('Invalid arguments provided')

        if bool(re.match('^tt', movie_id)) is False:
            raise ValueError('Movie id is not a valid movie id: {}'.format(movie_id))

        self.__movie_id = movie_id
        self.__release_date = release_date
        self.__country = country

    def movie_id(self) -> str:
        return self.__movie_id

    def release_date(self) -> datetime:
        return self.__release_date

    def country(self) -> str:
        return self.__country
