from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import csv


front_url = 'https://www.diningcode.com/profile.php?rid='
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
}
result = []
# f.write('Name,score,userscore,detail\n')
# f.write(search_input+','+'score'+','+'userscore'+','+'details'+'roca+''\n')
# tot_str=''
# for code in hrefs:
res_url = front_url + code
response = requests.post(res_url, headers=headers2)
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




