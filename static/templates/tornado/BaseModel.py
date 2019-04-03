# -*- coding: utf-8 -*-
# @File    : BaseUtils.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

import datetime
import mongoengine as model


class BaseModelDocument(model.Document):
    created = model.DateTimeField(default=datetime.datetime.now)
    updated = model.DateTimeField(default=datetime.datetime.now)

    meta = {
        'abstract': True,
        'ordering': ['-created'],
        'indexes': [
            {
                'fields': ['created'],
            },
            {
                'fields': ['updated'],
            },
        ]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
