#!/usr/bin/env python
#coding: utf-8

from app import create_app
from app.model import db
import unittest
from app.model.models import *


class BaseSuite(unittest.TestCase):

    #重写setUp，搭建测试环境，注意大小写
    def setUp(self):

        app = create_app()
        self.app = app
        self.client = app.test_client()

        db.init_app(app)
        db.app = app
        with app.app_context():    
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
