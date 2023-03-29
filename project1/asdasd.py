import requests
from bs4 import BeautifulSoup
 
param = '부산 봉래동'
 
url = 'https://www.diningcode.com/list.php?query='+param
 
html = requests.get(url)  ##requests를 이용해서 url의 html 파일을 가져옴
soup = BeautifulSoup(html.text, "html.parser")

stores = soup.find_all("a", class_="blink")
food_kinds = soup.findAll("span", attrs={"class":"stxt"})

for line1, line2 in zip(stores[1:], food_kinds[1:]):
    print(line1.get_text(), end= ': ')
    print(line2.get_text())
