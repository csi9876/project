from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import csv


re = '부산 '
search =  re + '봉래동'

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
f = open(f"res_data.csv", 'w')
f.write('Name,score,userscore,tag,roca,url,menu\n')
f.write(search+','+'score'+','+'userscore'+','+'tag'+','+'roca'+','+'url'+','+'menu''\n')
tot_str=''
for code in hrefs:
    herf_url = front_url + code
    response = requests.post(herf_url, headers=headers2)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('div',class_='tit-point').get_text().replace('\n', '')
    if ',' in name:
        name.replace(',', '.')
    roca = soup.find('li',class_='locat').get_text().replace('\n', '')

    try:
        menu = soup.find('ul', class_='list Restaurant_MenuList').get_text().replace('\n', ' ').replace(',', '')
        # print(menu)
    except:
        menu = '없음'
    
    for k in range(1, len(menu)-1):
        if menu[k].isdigit() and menu[k-1] == ' ':
            menu = menu[:k-1] + ':' + menu[k:]
    print(menu)
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

    tag = soup.find('div',class_='s-list pic-grade').find('div',class_='btxt').get_text().strip().replace(',',' ')
    temp = tag.find('| ') + 2
    tag = tag[temp:]
    f.write(name+','+str(score)+','+userscore+','+tag+','+roca+','+herf_url+','+menu+'\n')

f.close()

# df_ori = pd.read_csv('res_data.csv',encoding='cp949')
# df_ori = df_ori.fillna(' ')
# print(df_ori)

time.sleep(2) 