from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import csv

re = '부산'
search =  re + ' 명장동'
hrefs = []

for page in range(1,11):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
   }
    data = {
    'type': '',
    'query': search,
    'lat': '',
    'lng': '',
    'dis': '',
    'page': str(page),
    'chunk': '10',
    'rn': ''
    }
    response = requests.post('https://www.diningcode.com/2018/ajax/list.php', headers=headers, data=data)

    
    soup = BeautifulSoup(response.text, 'html.parser')
    stores = soup.find_all("a", class_="blink")
    for store in stores:
        hrefs.append(store['href'].split('rid=')[-1])
print(hrefs)

front_url = 'https://www.diningcode.com/profile.php?rid='
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
}
f = open('res_data.csv', 'w')
f.write('Name,score,userscore,detail,roca,url\n')
f.write(search+','+'score'+','+'userscore'+','+'details'+','+'roca'+','+'url''\n')
tot_str=''
for code in hrefs:
    href_url = front_url + code
    response = requests.post(href_url, headers=headers2)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('div',class_='tit-point').get_text().replace('\n', '')

    roca = soup.find('li',class_='locat').get_text().replace('\n', '')
    try:
        score = soup.find('p', class_='grade').find('strong')
        for i in score:
            if len(i) == 3:
                score = i
            else:
                score = '15점'

    except:
        score = '15점'


    try:
        userscore = soup.find(id='lbl_review_point')
        userscore = userscore.get_text()
    except:
        userscore = '리뷰없음'

    detail = soup.find('div',class_='s-list pic-grade').find('div',class_='btxt').get_text().strip().replace(',',' ')
    temp = detail.find('| ') + 2
    detail = detail[temp:]
    # print(detail)
    f.write(name+','+str(score)+','+userscore+','+detail+','+roca+','+href_url+'\n')
# f.write(search+','+'score'+','+'userscore'+','+'details'+'roca+''\n')
f.close()
df_ori = pd.read_csv('res_data.csv',encoding='cp949')
df_ori = df_ori.fillna(' ')
print(df_ori)

time.sleep(2) 