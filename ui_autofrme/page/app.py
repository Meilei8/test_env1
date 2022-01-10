# 是不是要启动app
from appium import webdriver

from ui_autofrme.page.base_page import BasePage
from ui_autofrme.page.main import Main


class App(BasePage):
    _package="com.xueqiu.android"
    _activity=".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            # 会报错，是因为声明和使用都是在同一行
            # caps = {}
            caps = dict()
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            # 为True每次都不清空数据
            caps['noReset'] = True
            # 初始化driver
            self._driver=webdriver.Remote(
                "http://127.0.0.1:4723/wd/hub",
                caps
            )

        else:
            # 如果发现有driver了，会直接启动activity,start_activity需要传两个参数：包名和activity名
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(5)
        # 返回自身
        return self

    # 定义一个返回类型
    def main(self)->Main:
        return Main(self._driver)


