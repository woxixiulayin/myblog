#/usr/bin/env python
# coding: utf-8

from flask.ext.script import Manager
from app import create_app
from app.model import db

# default prot number
PORT = 8888

app = create_app()
manager = Manager(app)


@manager.command
def run():
    app.host = '0.0.0.0'
    app.port = PORT
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Jackson/work/web/myblog/database/test.db'
    
    db.init_app(app)
    db.create_all()

    from livereload import Server
    server = Server(app)
    server.serve(port=PORT)


@manager.command
def create_db():
	db.create_all()

if __name__ == "__main__":
	manager.run()
