#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

import json
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def as_json(data):
    return mark_safe(json.dumps(data))
