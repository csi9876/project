from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import re
from time import sleep


location = ['부산광역시 영도구 봉래동2가 39-1 ','부산광역시 영도구 봉래동3가 17-2 ']

driver = webdriver.Chrome('chromedriver') # 열기
driver.implicitly_wait(3) # 3초안에 로드하면 넘어감, 못 하면 3초 기다림
driver.get('https://address.dawul.co.kr/#')
search_box = driver.find_element('xpath' , '//*[@id="input_juso"]')
search_button = driver.find_element('xpath' , '//*[@id="btnSch"]')
for i in location:
    search_box.send_keys(i) # 검색
    sleep(0.1)
    search_button.click() # 버튼 클릭
    sleep(0.1)
    loc = driver.find_element('xpath' , '//*[@id="insert_data_5"]')  # 검색
    print(loc.text) # 프린트