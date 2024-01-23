from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

searchKey = input('검색할 키워드 입력 :')

driver = webdriver.Chrome() #크롬드라이버 자신 크롬의 맞게 설정
driver.get("https://www.google.com/imghp?hl=ko&tab=ri&ogbl")

elem = driver.find_element('name', 'q')
elem.send_keys(searchKey)
elem.send_keys(Keys.RETURN)
time.sleep(3)

SCROLL_PAUSE_TIME = 3

last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try: 
          driver.find_element(".mye4qd").click()
        except:
           break
        
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(3)
        imgurl = driver.find_element(By.CSS_SELECTOR, ".iPVvYb").get_attribute("src")
        urllib.request.urlretrieve(imgurl,"호날두" + str(count)+ ".jpg")
        count = count + 1
    except:
        pass

driver.close()