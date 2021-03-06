
from flask import Blueprint

from voyager.views import index
from voyager.views import sailors
from voyager.views import boats
from voyager.views import voyages
from voyager.views import boats_by_popularity
from voyager.views import sailors_who_sailed
from voyager.views import boat_sailed_by
from voyager.views import given_sail_date
from voyager.views import given_color
from voyager.views import add_sailor
from voyager.views import add_boat
from voyager.views import add_voyage



blueprint = Blueprint('views', __name__)
index.views(blueprint)
sailors.views(blueprint)
boats.views(blueprint)
voyages.views(blueprint)
boats_by_popularity.views(blueprint)
sailors_who_sailed.views(blueprint)
boat_sailed_by.views(blueprint)
given_sail_date.views(blueprint)
given_color.views(blueprint)
add_sailor.views(blueprint)
add_boat.views(blueprint)
add_voyage.views(blueprint)


def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

