#!/usr/bin/env python
#!coding:utf-8

from app.model import db
from app.model.models import *


class DATA_API(object):

    def get_all_blogs(self):
        return Blog.query.all()

    def creat_blog(self, user, title, content):
        return Blog(user, title, content)
