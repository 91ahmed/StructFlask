from flask import render_template

class HomeController:

	def index():
		return render_template('home.html')