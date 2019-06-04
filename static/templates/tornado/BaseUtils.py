# -*- coding: utf-8 -*-
# @File    : BaseUtils.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

import datetime
import mongoengine_utils as model


class BaseUtils(model.BaseDocument):
    created = model.DateTimeField()
    updated = model.DateTimeField(pre_update=datetime.datetime.now)
