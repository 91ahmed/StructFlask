from flask import render_template
from sqlalchemy import select
from model.Admins import Admins

class AdminsController:

	def index():
		# get data from database
		stmt = select(Admins)
		result = Admins.connect.execute(stmt).fetchall()

		# render template
		return render_template('admins.html', data=result)