import click
from database.persist_decorator import persist_decorator
from movie.cli import movie_group
from movie import omdb_api
from movie.MovieDetails import MovieDetails
from movie.movie_repository import insert_or_update_movie_details, find_all_movie_details

@movie_group.command('update_all_movies')
@persist_decorator
def update_all_movies() -> None:
    movies = find_all_movie_details()
    from_api = __get_details(movies)

    __persist_movies(from_api)

def __get_details(movies : dict) -> tuple:
    movie_collection = []

    for movie in movies:
        id = movie['movie_id']
        details = omdb_api.get_movie(id)

        click.echo('found movie {}'.format(id))

        if details is None:
            click.echo('could not find {}'.format(id))
            continue

        movie_collection.append(details)

    return movie_collection

def __persist_movies(collection: tuple) -> None:
    for movie in collection :
        insert_or_update_movie_details(movie)
