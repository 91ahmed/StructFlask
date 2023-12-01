from controller import HomeController
from controller import UsersController

def routes(app):

	@app.route('/', methods=['GET'])
	def route1():
		return HomeController.index()

	@app.route('/users', methods=['GET'])
	def route2():
		return UsersController.index()