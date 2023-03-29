from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import re
from time import sleep



df1 = pd.read_csv('res_data0.csv', encoding='cp949')
roca = df1['roca']
print(roca)

# location = ['부산광역시 영도구 봉래동2가 39-1 ','부산광역시 영도구 봉래동3가 17-2 ']


driver = webdriver.Chrome('chromedriver') # 열기
driver.implicitly_wait(3) # 3초안에 로드하면 넘어감, 못 하면 3초 기다림
driver.get('https://address.dawul.co.kr/#')
search_box = driver.find_element('xpath' , '//*[@id="input_juso"]')
search_button = driver.find_element('xpath' , '//*[@id="btnSch"]')

list1 = []
for i in roca:
    search_box.send_keys(i) # 검색
    sleep(0.1)
    search_button.click() # 버튼 클릭
    sleep(0.1)
    loc = driver.find_element('xpath' , '//*[@id="insert_data_5"]')  # 검색
    print(loc.text) # 프린트
    list1.append(loc.text)


df1['coordinate'] = list1

df1.to_csv("df1.csv", index = False)