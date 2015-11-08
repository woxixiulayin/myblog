#/usr/bin/env python
# coding: utf-8

from flask.ext.script import Manager
from app import creat_app

#default prot number
PORT = 8888

app = creat_app()
manager = Manager(app)

@manager.command
def run():
	app.host = '0.0.0.0'
	app.port = PORT
	app.debug = True

	from livereload import Server
	server = Server(app)
	server.serve(port=PORT)


if __name__ == "__main__":
	manager.run()
