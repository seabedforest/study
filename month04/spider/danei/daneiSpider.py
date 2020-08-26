"""
登录达内
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='http://www.tmooc.cn/')


driver.find_element_by_xpath('//*[@id="login_xxw"]').click()
time.sleep(0.5)
set_node=driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]')
ActionChains(driver).move_to_element(to_element=set_node).perform()



