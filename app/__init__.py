#/usr/bin/env python
# coding: utf-8

from flask import Flask
from .controllers.site import bp


def creat_app():
	app = Flask(__name__)

	app.register_blueprint(bp)

	return app