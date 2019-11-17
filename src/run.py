from flask import Flask
from movie.cli import movie_group
from pathlib import Path
from dotenv import load_dotenv
from frontend import controller
from database import db
from flask import render_template
import os

env = Path('../') / '.env'
load_dotenv(dotenv_path=env)

app = Flask(__name__)
app.cli.add_command(movie_group)

def system_error(e):
    return render_template('system/system-error.html', error=e), 404

app.add_url_rule('/', view_func=controller.index)
app.add_url_rule('/movie/<movie_id>', view_func=controller.movie)
app.register_error_handler(404, system_error)
