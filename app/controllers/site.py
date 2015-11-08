# coding: utf-8

from flask import render_template, Blueprint

bp = Blueprint('site', __name__)

@bp.route('/')
def index():
	return render_template("index.html")