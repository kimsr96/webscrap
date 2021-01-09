import requests
from bs4 import BeautifulSoup

url ="https://news.naver.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

news = soup.find_all("div",attrs={"class":"hdline_article_tit"})
for i in range(0,3):
    link = news[i].find("a")["href"]
    print(f"{i+1}.{''.join(news[i].get_text().split())}")
    print("https://news.naver.com/"+ link)

#헤드라인 뉴스
#1. 무슨 무슨 일이...
# (링크 :// https)
#2. 어떤 어떤 일이....
