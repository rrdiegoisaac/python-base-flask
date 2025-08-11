from flask import Flask, jsonify
from .routes import *
from .config import s

def create_app(test_mode=False):
    app = Flask(__name__, instance_relative_config=True)
 
    if test_mode:
        app.config.from_object(config["test"])
    else:
        app.config.from_object(config["development"])

    app.register_blueprint(main)

    return app


