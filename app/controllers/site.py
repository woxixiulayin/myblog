# coding: utf-8

from flask import render_template, Blueprint
from ..utils.data_api import DATA_API


data = DATA_API()

bp = Blueprint('site', __name__)


@bp.route('/')
@bp.route('/blogs')
def index():
    blogs = data.get_all_blogs()
    return render_template("index.html", blogs=blogs)


