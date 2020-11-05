#!/user/bin/python
# _*_ coding:utf-8 _*_
from django.conf.urls import url

from spider import views

__author__ = "super.gyk"

urlpatterns = [
    url(r'^add/$', views.api_add, name="wechat.api_add"),
    url(r'^topic/add/$', views.api_topic_add, name="wechat.api_topic_add"),
    url(r'^search/$', views.api_search, name="wechat.api_search"),

]