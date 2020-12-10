#!/user/bin/python
# _*_ coding:utf-8 _*_
import json
import time

from selenium import webdriver

__author__ = "super.gyk"


class WeChatSpider(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        self.chromedriver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver'
        self.driver = webdriver.Chrome(self.chromedriver)
        self.user = "1187757450@qq.com"
        self.pwd = "tianxiawushuang8"
        self.gzlist = ['郑州日报', "参考消息"]

    def wechat_login(self):
        """
        登录微信
        :return:
        """
        post = {}
        print("启动浏览器，打开微信登录界面")

        self.driver.get('https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=182536812')
        # 等待5s
        time.sleep(50)
        print("正在输入微信公众号登录账号密码...")
        # 清空账号框中的内容
        self.driver.find_element_by_xpath("./*//input[@name='account']").clear()
        # 自动填入登录用户名
        self.driver.find_element_by_xpath("./*//input[@name='account']").send_keys(self.user)
        # 清空密码框中的内容
        self.driver.find_element_by_xpath("./*//input[@id='password']").clear()
        # 自动填入登录密码
        self.driver.find_element_by_xpath("./*//input[@id='password']").send_keys(self.pwd)

        # 在自动输完密码之后需要手动点一下记住我
        print("请在登录界面点击:记住账号")
        time.sleep(10)
        # 自动点击登录按钮进行登录
        self.driver.find_element_by_xpath("./*//a[@class='btn_login']").click()
        # 拿手机扫二维码！
        print("请拿手机扫码二维码登录公众号")
        time.sleep(20)
        print("登录成功")
        # 重新载入公众号登录页，登录之后会显示公众号后台首页，从这个返回内容中获取cookies信息
        self.driver.get('https://mp.weixin.qq.com/')
        # 获取cookies
        cookie_items = self.driver.get_cookies()

        # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
        for cookie_item in cookie_items:
            post[cookie_item['name']] = cookie_item['value']
        cookie_str = json.dumps(post)
        with open('cookie.txt', 'w+', encoding='utf-8') as f:
            f.write(cookie_str)
        print("cookies信息已保存到本地")

    def spider(self):
        """
        创作管理 -> 图文素材 -> 新的创作 -> 图文消息- > 超链接
        :return:
        """
        print("进入首页")
        self.driver.get('https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=182536812')

        print("点击图文素材")
        self.driver.find_element_by_xpath(
            "./*//a[@class='weui-desktop-menu__link js_nav_item weui-desktop-menu__link_current']").click()
        print("点击新的创作")
        self.driver.find_element_by_xpath("./*//div/i[@class='weui-desktop-card__icon-add']")
        print("点击图文消息")
        self.driver.find_element_by_xpath("./*//div[@class='preview_media_add_panel']//li[@title='图文消息']")
        print("点击超链接")
        self.driver.find_element_by_xpath("//li[@id='js_editor_insertlink']")
        print("点击选择其他公众号")
        self.driver.find_element_by_xpath(
            "//p/button[@class='weui-desktop-link-btn weui-desktop-link weui-desktop-btn weui-desktop-btn_default']")
        time.sleep(100)


if __name__ == "__main__":
    spider = WeChatSpider()
    spider.spider()
