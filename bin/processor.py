# -*- coding: utf-8 -*-
__author__ = 'yankai.guan'
# 加载django环境
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'woas.settings'
import django

django.setup()

import json
from django.conf import settings
from spider.models import Topic
from spider.processors import DjangoModelBackend
from utils.redis_util import get_redis
import logging

logger = logging.getLogger()


class Processor():
    def __init__(self):
        self.pools = {}

    def get_backends(self):
        backend = DjangoModelBackend(Topic)
        return [backend]

    def process(self, data):
        backends = self.get_backends()
        for backend in backends:
            backend.process(data)

    def run(self):
        r = get_redis()
        if settings.CRAWLER_DEBUG:
            r.delete(settings.CRAWLER_CONFIG["processor"])
        while True:
            try:
                rsp = r.brpop(settings.CRAWLER_CONFIG["processor"])
            except Exception as e:
                print(e)
                continue

            data = json.loads(rsp[1])
            logger.info(json.dumps(data, encoding="UTF-8", ensure_ascii=False))
            self.process(data)


if __name__ == '__main__':
    processor = Processor()
    processor.run()
