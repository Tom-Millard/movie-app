from database import db
from movie.MovieRelease import MovieRelease
from movie.MovieDetails import MovieDetails
from typing import Union
import json

def find_all_movie_details() -> dict :
  sql = 'SELECT id, movie_id, details FROM movie_details'

  db.cursor.execute(sql)

  return db.cursor

def find_all_movies_from_last_two_weeks_onwards() -> dict : 
  sql = '' \
      'SELECT' \
      ' movie_details.*, movie_releases.release_date, movie_releases.country' \
      ' FROM' \
      ' movie_details' \
      ' JOIN' \
      ' movie_releases ON movie_details.movie_id = movie_releases.movie_id' \
      ' WHERE' \
      ' movie_releases.release_date >= NOW() - INTERVAL \'2 WEEKS\' ' \
      ' ORDER BY' \
      ' movie_releases.release_date ASC'

  db.cursor.execute(sql)

  return db.cursor


def find_one_movie(movie: str) -> MovieDetails:
    sql = 'SELECT movie_id, details FROM movie_details WHERE movie_id = %s'

    db.cursor.execute(sql, (movie,))

    movie = db.cursor.fetchone()

    if (movie is None) :
        raise Exception('{} not found'.format(movie))

    return MovieDetails(movie[0], movie[1])


def find_one_release_date(movie: str, country : str) -> MovieRelease:
    sql = 'SELECT movie_id, release_date, country FROM movie_releases WHERE movie_id = %s AND country = %s'

    db.cursor.execute(sql, (movie, country))

    movie = db.cursor.fetchone()

    if (movie is None) :
        raise Exception('{} not found'.format(movie))

    return MovieRelease(movie[0], movie[1], movie[2])

def insert_or_update_movie_release(release: MovieRelease) -> dict :
    sql = '' \
          'INSERT INTO movie_releases (movie_id, release_date, country) VALUES (%s, %s, %s)' \
          'ON CONFLICT (movie_id, country)' \
          'DO UPDATE SET release_date = EXCLUDED.release_date, updated_at = now()'

    db.cursor.execute(
        sql,
        (release.movie_id(), release.release_date(), release.country())
    )

    return db.cursor


def insert_or_update_movie_details(details: MovieDetails) -> dict:
    sql = '' \
        'INSERT INTO movie_details (movie_id, details) VALUES (%s, %s)' \
        'ON CONFLICT (movie_id)' \
        'DO UPDATE SET updated_at = now(), details = %s'

    db.cursor.execute(
        sql,
        (
            details.movie_id(), 
            json.dumps(details.details()),
            json.dumps(details.details())
        )
    )

    return db.cursor
