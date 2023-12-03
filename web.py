from controller.HomeController import HomeController
from controller.AdminsController import AdminsController

'''
	Notes: when you using routes
	============================
	1. The return type must be a string, dict, tuple, Response instance, or WSGI callable.
	2. The function should either returned None or ended without a return statement.
	3. The route functions should have different names. like (def route1():, def route2():).
'''
def routes(app):

	@app.route('/', methods=['GET'])
	def route1():
		return HomeController.index()

	@app.route('/admins', methods=['GET'])
	def route2():
		return AdminsController.index()