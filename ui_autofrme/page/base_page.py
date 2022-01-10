# base_page本质上是对driver操作的封装
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # _driver被定义为实例变量，好处：子类可以使用
    _driver:WebDriver

    # 定义一个初始化的构造方法
    def __init__(self,driver:WebDriver=None):
        # 没有WebDriver传进来，_driver就是None
        self._driver=driver

    # locator：定位方式，value：表达式
    def find(self,locator,value):
        return self._driver.find_element(locator,value)

    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()

    