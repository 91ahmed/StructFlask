from controller.BaseController import BaseController
from flask import render_template

class HomeController(BaseController):

	def index():
		# some data
		names = ['data1', 'data2', 'data3']
		# render the template and pass the data to the view
		return render_template('home.html', data=names)