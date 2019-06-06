from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 静默模式
# 打开chrome浏览器
driver = webdriver.Chrome(options=option)
driver.get("https://www.learning.gov.cn/index.php")
print(driver.title)
sleep(2)

driver.close()
