"""
    打开浏览器，输入百度
"""
from selenium import webdriver

# 1.创建浏览器对象->打开浏览器
# driver = webdriver.Chrome()
# driver.get(url='http://www.baidu.com')

driver = webdriver.PhantomJS()
driver.get(url='http://www.baidu.com')
driver.save_screenshot('baidu.png')
