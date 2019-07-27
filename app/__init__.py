from flask import Flask

from app.site.routes import site
from app.api.routes import api


def create_app(db):
    """
    Creating a Flask application and registering an extensions and blueprints

    :return: Flask object
    """
    app = Flask(__name__)

    # extensions registrations
    db.app = app
    db.init_app(app)

    # blueprints registration
    app.register_blueprint(site)
    app.register_blueprint(api, url_prefix='/api')
    return app



