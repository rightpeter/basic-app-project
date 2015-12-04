#!/usr/bin/env python
# -*- coding: utf-8 -*-

from baseHandler import BaseHandler
from operations.routes import route
from tornado import gen
from models.model import TestModel


@gen.coroutine
@route(r'/$', name='index')
class MainHandler(BaseHandler):
    def get(self):
        self.write('Hello TourList!')


@route(r'/heihei$', name='heihei')
class HeiHeiHandler(BaseHandler):
    def get(self):
        self.write('Hei Hei')


@route(r'/test_model$', name='test_model')
class TestModelHandler(BaseHandler):
    def get(self):
        res = 'test_model title: <br>'
        for test in TestModel.objects:
            res += '<br>' + test.title
        self.write(res)

    def post(self):
        title = self.get_argument('title')
        text = self.get_argument('title')
        tmp_model = TestModel(title, text)
        tmp_model.save()
