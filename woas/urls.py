"""woas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from spider import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('ckeditor_uploader.urls')),
    path(r'', views.fist_not_index, name="wechat.not_index"),
    path(r'index/', views.index, name="wechat.index"),
    path(r'wechat/', include('spider.urls')),
    path(r'api/wechat/', include('spider.api_urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
