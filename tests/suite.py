#!/usr/bin/env python
#coding: utf-8

from app import create_app
from app.model import db
import unittest

class BaseSuite(unittest.TestCase):
    def setUp(self):

        app = create_app()
        self.app = app
        self.client = app.test_client()

        with app.app_context():
            db.init_app(app)
            db.drop_all()
            db.create_all()


    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
