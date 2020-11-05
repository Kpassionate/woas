from django.contrib import admin

from spider.models import Wechat, Topic, Proxy, Word, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'last_login']


@admin.register(Wechat)
class WechatAdmin(admin.ModelAdmin):
    list_display = ['name', 'wechatid']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['wechat', 'uniqueid', 'title']
    list_filter = ['title']


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ['host', 'port', 'create_time']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['text']

