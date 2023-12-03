from flask import render_template

class HomeController:

	def index():
		# some data
		names = ['ahmed', 'mohamed', 'hossam']
		# render the template and pass the data to the view
		return render_template('home.html', data=names)