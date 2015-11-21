# coding: utf-8
from .suite import BaseSuite
from app.model.models import *

class TestSite(BaseSuite):

    def test_index(self):
        rv = self.client.get('/')
        assert rv.status_code == 200

    def test_db(self):


        u = User(name='liuzhigang', email='zhigang@qq.com')
        db.session.add(u)
        db.session.commit()

        assert User.query.all()[0].name == 'liuzhigang'
