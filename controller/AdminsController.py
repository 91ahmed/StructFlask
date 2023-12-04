from controller.BaseController import BaseController
from flask import render_template
from flask import request
from sqlalchemy import select
from model.Admins import Admins

class AdminsController(BaseController):

	def index():
		# get data from database
		stmt = select(Admins)
		result = Admins.connect.execute(stmt).fetchall()

		username = None
		if request.method == 'POST':
			username = request.form['username']

		# render template
		return render_template('admins.html', data=result, username=username)