import os
from flask import Flask, request
from web import routes

views_path = os.path.abspath('view')

app = Flask(__name__, template_folder=views_path)

# Calling the application routes
routes(app)