# coding: utf-8

from flask import render_template, Blueprint
from ..model import db
from ..model.models import User


bp = Blueprint('site', __name__)

def test_db():
    user = User.query.first()
    print user

@bp.route('/')
def index():
    test_db()
    return render_template("index.html")