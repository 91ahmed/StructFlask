from flask import render_template
from sqlalchemy import select
from model.Admins import Admins

class AdminsController:

	def index():
		
		stmt = select(Admins)
		result = Admins.connect.execute(stmt).fetchall()

		print(result)

		return render_template('admins.html')