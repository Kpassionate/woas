#!/user/bin/python
# _*_ coding:utf-8 _*_

__author__ = "super.gyk"

from django import forms
from spider.models import Wechat


class WechatForm(forms.ModelForm):
    class Meta:
        model = Wechat
        fields = ['avatar', 'qrcode', 'name', 'wechatid', 'intro', 'frequency']


class WechatConfigForm(forms.ModelForm):
    class Meta:
        model = Wechat
        fields = ['frequency']
