from flask import render_template, abort
from movie.movie_repository import find_all_movies_from_last_two_weeks_onwards, find_one_movie, find_one_release_date
from movie.MovieDetails import MovieDetails
from datetime import datetime

def index():
  movies = find_all_movies_from_last_two_weeks_onwards()
  collection = {}

  for movie in movies:
    dt = movie['release_date']
    date_key = str(dt.year) + str(dt.month) + str(dt.day)
    date_key = datetime.strptime(date_key, '%Y%m%d')

    if date_key not in collection:
      collection[date_key] = []

    m = MovieDetails(movie['movie_id'], movie['details'])
    m.addReleaseDate(movie['country'], movie['release_date'])
    collection[date_key].append(m)

  return render_template('movie-list.html', movies=collection)

def movie(movie_id: str):
    try :
        movie = find_one_movie(movie_id)
        movie_release_date = find_one_release_date(movie_id, 'GB')
    except :
        abort(404, description="`{}`".format(movie_id))


    return render_template('movie.html', movie=movie, release=movie_release_date)
