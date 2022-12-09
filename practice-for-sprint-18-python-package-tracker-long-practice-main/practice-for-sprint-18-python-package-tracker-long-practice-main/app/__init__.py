from flask import (Flask, render_template)
from .config import Config
from .routes import root, package
app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(root.bp)

app.register_blueprint(package.bp)
