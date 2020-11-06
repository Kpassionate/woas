# woas
wechat office account spider

使用Django2.1.7版本
使用selenium

本地项目启动使用 python manage runserver

启动爬虫

python bin/downloader.py
python bin/extractor.py
python bin/processor.py
python bin/scheduler.py

自定义模板标签时要注意 templatetags需要放在app里面，否则会报错