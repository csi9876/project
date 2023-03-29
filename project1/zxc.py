from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import csv

# front_url = 'https://www.diningcode.com/profile.php?rid='
#     headers2 = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
#     }
#     f = open(f"res_data{abc}.csv", 'w')
#     f.write('Name,score,userscore,detail\n')
#     f.write(search_input+','+'score'+','+'userscore'+','+'details'+'roca+''\n')
#     tot_str=''
#     for code in hrefs:
#         res_url = front_url + code
#         response = requests.post(res_url, headers=headers2)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         name = soup.find('div',class_='tit-point').get_text().replace('\n', '')
#         roca = soup.find('li',class_='locat').get_text().replace('\n', '')
#         try:
#             score = soup.find('p', class_='grade').find('strong')
#             for i in score:
#                 if len(i) == 3:
#                     score = i
#                 else:
#                     score = '15점'

#         except:
#             score = '15점'


#         try:
#             userscore = soup.find(id='lbl_review_point')
#             userscore = userscore.get_text()
#         except:
#             userscore = '리뷰없음'

#         detail = soup.find('div',class_='s-list pic-grade').find('div',class_='btxt').get_text().strip().replace(',',' ')
#         f.write(name+','+str(score)+','+userscore+','+detail+','+roca+'\n')
    
#     f.close()

#     time.sleep(2) 



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://map.naver.com/v5/search")

# # 팝업 창 제거
# driver.find_element(By.CSS_SELECTOR, "button#intro_popup_close").click()

# # 검색창에 검색어 입력하기
# # search_box = driver.find_element_by_css_selector("div.input_box>input.input_search")
# search_box = driver.find_element( By.CSS_SELECTOR, "div.input_box>input.input_search",)
# search_box.send_keys("부산광역시 연제구 거제동 242-23 ")

# time.sleep(3)

# # 검색버튼 누르기
# search_box.send_keys(Keys.ENTER)

# # 크롤링
# for p in range(20):
#     # 5초 delay
#     time.sleep(2)
    
#     js_script = "document.querySelector(\"body > app > layout > div > div.container > div.router-output > "\
#                 "shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar\").innerHTML"
#     raw = driver.execute_script("return " + js_script)

#     html = BeautifulSoup(raw, "html.parser")

#     contents = html.select("div > div.ps-content > div > div > div .item_search")
#     for s in contents:
#         search_box_html = s.select_one(".search_box")

#         name = search_box_html.select_one(".title_box .search_title .search_title_text").text
#         print("식당명: " + name)
#         try:
#             phone = search_box_html.select_one(".search_text_box .phone").text
#         except:
#             phone = "NULL"
#         print("전화번호: " + phone)
#         address = search_box_html.select_one(".ng-star-inserted .address").text
#         print("주소: " + address)

#         print("--"*30)
#     # 다음 페이지로 이동
#     try:
#         next_btn = driver.find_element( By.CSS_SELECTOR, "button.btn_next")
#         next_btn.click()
#     except:
#         print("데이터 수집 완료")
#         break

# # 크롭 웹페이지를 닫음
# print(1)
# driver.close()




# # 네이버 지도 데이터 수집하기
# from selenium import webdriver

# driver = webdriver.Chrome("./chromedriver")
# # 구버전 네이버지도 접속
# driver.get("https://map.naver.com/v5/?c=15,0,0,0,dh")

# driver.find_elements_by_css_selector("button.btn_close")[1].click()
# ##################################################

# # 검색창에 검색어 입력하기 // 검색창: input#search-input
# search_box = driver.find_element_by_css_selector("input#search-input")
# search_box.send_keys("부산광역시 영도구 봉래동2가 39-1 ")
# # 검색버튼 누르기 // 검색버튼: button.spm
# search_button = driver.find_element_by_css_selector("button.spm")
# search_button.click()

# # 검색버튼 누르기 // 검색버튼: button.spm
# search_button = driver.find_element_by_css_selector("button.spm")
# search_button.click()

# # 컨테이너(가게 정보) 수
# stores = driver.find_elements_by_css_selector("div.lsnx")
# for store in stores:
#     # 세부 데이터 수집
#     name = store.find_element_by_css_selector("dt > a").text
#     addr = store.find_element_by_css_selector("dd.addr").text
#     phone = store.find_element_by_css_selector("dd.tel").text
    
#     print(name, addr, phone)

    # 네이버 지도 데이터 수집하기
# from selenium import webdriver

# ##################################################
# # 파이썬 내부 라이브러리 time을 사용합니다.
# # time: 시간과 관련된 여러가지 기능을 포함합니다.
# import time
# ##################################################

# driver = webdriver.Chrome("./chromedriver")
# # 구버전 네이버지도 접속
# driver.get("https://map.naver.com/v5/?c=15,0,0,0,dh")
# # !!!추가//네이버 지도 업데이트 후 안내메시지 끄기##########
# # 무시하고 진행해주세요.
# driver.find_elements( By.CSS_SELECTOR,"button.btn_close").click()
# ##################################################

# #3. 검색창에 검색어 입력하기 // 검색창: input#search-input
# search_box = driver.find_element( By.CSS_SELECTOR, "input#search-input")
# search_box.send_keys("치킨")
# #4. 검색버튼 누르기 // 검색버튼: button.spm
# search_button = driver.find_element( By.CSS_SELECTOR,"button.spm")
# search_button.click()

# ##################################################
# # 1초의 지연시간을 줍니다. 
# time.sleep(1)
# ##################################################

# # 컨테이너(가게 정보) 수
# stores = driver.find_elements( By.CSS_SELECTOR,"div.lsnx")
# for store in stores:
#     # 세부 데이터 수집
#     name = store.find_element( By.CSS_SELECTOR,"dt > a").text
#     addr = store.find_element( By.CSS_SELECTOR,"dd.addr").text
#     phone = store.find_element( By.CSS_SELECTOR,"dd.tel").text

#     print(name, addr, phone)