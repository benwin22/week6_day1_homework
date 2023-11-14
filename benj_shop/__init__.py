from flask import Flask
from .blueprints.site.routes import site

app = Flask(__name__)

# using a decorator to create our first route
# @app.route("/")
# def hello_world():
#     return "<p>Hello World!</p>"

app.register_blueprint(site)