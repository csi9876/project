from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import csv


# 위치가 담겨있는 csv파일 열기
f = open('pusan_loc.csv','r', encoding="utf-8" )
rdr = csv.reader(f)
 
roc = []
for line in rdr:
    roc.append(line[1])
 
f.close()
roc = roc[1:69]
# print(len(roc))
print(roc)

for abc in range(len(roc)):
    print(roc[abc])

    # re = '부산 '
    search_input =  '부산 ' + roc[abc]

    hrefs = []

    for page in range(1,11):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
    }
        data = {
        'type': '',
        'query': search_input,
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
    f.write('Name,score,userscore,detail,roc\n')
    f.write(search_input+','+'score'+','+'userscore'+','+'details'+'roc+''\n')
    tot_str=''
    for code in hrefs:
        res_url = front_url + code
        response = requests.post(res_url, headers=headers2)
        soup = BeautifulSoup(response.text, 'html.parser')
        res_name = soup.find('div',class_='tit-point').get_text().replace('\n', '')

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
        f.write(res_name+','+str(score)+','+userscore+','+detail+','+roca+'\n')
    # f.write(search_input+','+'score'+','+'userscore'+','+'details'+'roca+''\n')
    f.close()
    # df_ori = pd.read_csv('res_data.csv',encoding='cp949')
    # df_ori = df_ori.fillna(' ')
    # print(df_ori)

    time.sleep(2) 