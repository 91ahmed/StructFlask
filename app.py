'''
	Python: v3.10.5
	PiP: v23.3.1 (Package installer / manager)
	Flask: v2.1.3 (WSGI web application micro framework)
	Jinja2: v3.1.2 (Templating engine)
	SQLAlchemy: v2.0.23 (ORM: Object Relational Mapper)
	psycopg2: v2.9.9 (PostgreSQL database adapter)
'''

import os
from flask import Flask, request
from web import routes

views_path = os.path.abspath('view')

app = Flask(__name__, template_folder=views_path)

# Calling the application routes
routes(app)