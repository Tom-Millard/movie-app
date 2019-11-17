import click
from movie.cli import movie_group
from movie import omdb_api
from movie.movie_repository import insert_or_update_movie_details
from movie.movie_repository import find_all_movie_details
from database.persist_decorator import persist_decorator

@movie_group.command('get_movie')
@click.argument('movie_id')
@persist_decorator
def get_movie(movie_id: str) -> None:
  click.echo(movie_id)
  movie = omdb_api.get_movie(movie_id)

  if movie is None:
      click.echo('unable to import')
      return None

  insert_or_update_movie_details(movie)

