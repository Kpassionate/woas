"""
Django settings for woas project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1.7/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#ts!rv!c!7pf(d&=2#fdu56b1$ff5-x9u#4&fp5=-x4g!mbu16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spider.apps.SpiderConfig',
    'ckeditor',
    'ckeditor_uploader',
]

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 800,
    'height': 600,
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'woas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'libraries':{
            #     'my_customer_tags':  'woas.templatetags.paginator',
            # }
        },
    },
]

WSGI_APPLICATION = 'woas.wsgi.application'
AUTH_USER_MODEL = 'spider.user'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'woas',
#         'HOST': '127.0.0.1',
#         'PORT': 3306,
#         'USER': 'root',
#         'PASSWORD': '123456',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'woas',
        'HOST': 'ppxia.work',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1.7/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 日志配置
import time
cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}
# crawler config
CRAWLER_DEBUG = False
CRAWLER_CONFIG = {
    'scheduler': 'unicrawler:scheduler',
    'downloader': 'unicrawler:downloader',
    'extractor': 'unicrawler:extractor',
    'processor': 'unicrawler:processor',
    'global_limit_speed': 'unicrawler:global_limit_speed',
    'antispider': 'unicrawler:antispider'
}
CRAWLER_GLOBAL_LIMIT_SPEED = 20 * 1000 # 毫秒

# aliyun oss2
OSS2_ENABLE = False
OSS2_CONFIG = {
    "ACCESS_KEY_ID": "",
    "ACCESS_KEY_SECRET": "",
    "ENDPOINT": "",
    "BUCKET_DOMAIN": "oss-cn-beijing.aliyuncs.com",
    "BUCKET_NAME": "pythonzone",
    "IMAGES_PATH": "images/",
    "VIDEOS_PATH": "videos/",
    "CDN_DOMAIN": "pystats.bowenpay.com"
}
LOGIN_URL = '/admin/login/'

REDIS_OPTIONS = {
    'host': 'localhost',
    'port': 6379,
    'password': '',
    'db': 4
}

# Internationalization
# https://docs.djangoproject.com/en/2.1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'


SUIT_CONFIG = {
    'ADMIN_NAME': '微信公众号爬虫',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'SEARCH_URL': '',
    'MENU': (
        {'label': '账户管理', 'url': 'spider.user'},

        {'label': '公众号', 'url': 'spider.wechat'},
        {'label': '文章', 'url': 'spider.topic'},

        {'label': '代理', 'url': 'spider.proxy'},
        {'label': '关键词', 'url': 'spider.word'},

    )
}