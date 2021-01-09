import requests
from bs4 import BeautifulSoup

url ="https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li", limit=3)

for idx,news in enumerate(news_list):
    title = news.find_all("dt")[1].find("a").get_text()
    link = news.find("a")["href"]
    print(title.strip())
    print(link)