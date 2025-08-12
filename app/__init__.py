from flask import Flask, jsonify
from .config import s, config
from .routes import (main)
from .models import (db, migrate, Usuario)

def create_app(test_mode=False):
    app = Flask(__name__, instance_relative_config=True)
 
    if test_mode:
        app.config.from_object(config["test"])
    else:
        app.config.from_object(config["development"])

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app


