#!/usr/bin/env python
# encoding=utf-8

from mongoengine import *


class TestModel(Document):

    """Test Mongoengine"""

    title = StringField(required=True)
    text = StringField()
