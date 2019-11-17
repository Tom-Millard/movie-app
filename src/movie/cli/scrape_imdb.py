import click
from movie.cli import movie_group
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import datetime
from typing import Union
from movie.MovieRelease import MovieRelease
from movie import movie_repository, omdb_api
from database.persist_decorator import persist_decorator

@movie_group.command('scrape_imdb')
@persist_decorator
def scrape_imdb() -> None:
    content = __get_imdb_html()

    if content is None:
        click.echo('Nothing to do, something went wrong with the scrape')
        return None

    soup = BeautifulSoup(content, 'html.parser')
    movies: list = __process_content(soup)

    for m in movies: # type: MovieRelease
        movie_repository.insert_or_update_movie_release(m)
        click.echo('Inserts {} into db'.format(m.movie_id()))
        details = omdb_api.get_movie(m.movie_id())
        movie_repository.insert_or_update_movie_details(details)

def __get_imdb_html() -> Union[str, None]:
    try:
        with closing(get('https://www.imdb.com/calendar?region=GB', stream=True)) as response:
            if response.status_code == 200 :
                return response.content.lower()
            else:
                return None

    except RequestException as e:
        return None

def __process_content(content: BeautifulSoup) -> list:
    collection = []
    main = content.select('#main')

    if len(main) is 0:
        raise ValueError('Main is not set in this chunk of HTML')

    for h4 in content.select('#main')[0].find_all('h4'):
        date_string = h4.get_text()
        date_string_as_date = datetime.datetime.strptime(date_string, '%d %B %Y')

        for li in h4.find_next().find_all('li'):
            for a in li.find_all('a'):
                href = a.get_attribute_list('href')

                if len(href) is 0:
                    continue

                href = href[0].split('/')

                if len(href) < 4:
                    continue

                try:
                    movie = MovieRelease(href[2], date_string_as_date, 'GB')
                    click.echo('movie {} found'.format(href[2]))
                except ValueError as e:
                    click.echo('unable to inport information about {}'.format(href[2]))
                    continue

                collection.append(movie)

    return collection


