from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://maoyan.com/board/4')
# 基准xpath: 匹配所有电影信息的dd节点对象列表
dd_list = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
for dd in dd_list:
    item = {}
    print(dd.text)
    print('*'*50)
