from flask.cli import AppGroup


def __import_commands() -> None :
    import movie.cli.get_movie
    import movie.cli.scrape_imdb
    import movie.cli.update_all_movies


movie_group = AppGroup('movie')
__import_commands()
