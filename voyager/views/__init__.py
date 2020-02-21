
from flask import Blueprint

from voyager.views import index
from voyager.views import sailors
from voyager.views import boats
from voyager.views import voyages
from voyager.views import boats_by_popularity
from voyager.views import sailors_who_sailed

blueprint = Blueprint('views', __name__)
index.views(blueprint)
sailors.views(blueprint)
boats.views(blueprint)
voyages.views(blueprint)
boats_by_popularity.views(blueprint)
sailors_who_sailed.views(blueprint)


def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

