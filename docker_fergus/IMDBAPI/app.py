from flask import Flask

from api.config import config
from api.routes import routes


# Instantiate and initialise our Flask app
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Register the SQLAlchemy extension
    from api.models import db
    db.init_app(app)

    # Register the Marshmallow extension
    from api.schemas import ma
    ma.init_app(ma)

    # Expose our routes
    app.register_blueprint(routes)

    return app


# When this file is run as a script, run the Flask app
# This adds support for running our app without the Flask CLI
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')
