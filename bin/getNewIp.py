# -*- coding: utf-8 -*-

__author__ = 'yankai.guan'
import socket
import time
from urllib import parse, request


def get_ip():
    ip_list = socket.gethostbyname_ex(socket.gethostname())
    for itemList in ip_list:
        if isinstance(itemList, list):
            for ip in itemList:
                if ip not in ['192.168.11.58']:
                    save_ip(ip)


def save_ip(exip):
    if exip:
        print("new ip:", exip)
        params = parse.urlencode({'host': exip, 'port': 8000}).encode('utf-8')
        f = request.urlopen("http://127.0.0.1:8000/wechat/proxy/1/edit/", params)
        f.read()
    print("休息3秒")
    time.sleep(3)


if __name__ == '__main__':
    """
    每3秒修改一次host,以防止被禁
    """
    while True:
        try:
            get_ip()
        except Exception as e:
            print(e)
        finally:
            print("重新更换！")
