from controller import HomeController
from controller import UsersController

def routes(app):

	@app.route('/')
	def route1():
		return HomeController.index()

	@app.route('/users')
	def route2():
		return UsersController.index()
