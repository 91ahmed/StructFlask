from flask import Flask
from web import routes

app = Flask(__name__)
routes(app)