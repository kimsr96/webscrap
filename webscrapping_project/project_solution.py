import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    soup = create_soup
    soup.find("p", attrs={"class":"cast_txt"}).get_text()
    curr_temp = soup.find("p", attrs={"class":"info_temperate"}).get_text().replace("도씨", "")
    min_temp = soup.find("p", attrs={"class":"info_temperate"}).get_text()
    max_temp = soup.find("p", attrs={"class":"info_temperate"}).get_text()

def scrap_headline_news():
    print("[헤드라인 뉴스]")
    url ="https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.div.a.get_text().strip()
        link = url + news.find("a")["href"]
        print("{}.{}".format(index+1, title))
        print(" (링크 : {}".format(link))
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url ="https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li", limit=3)
    #3개 까지만 가져오기
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 #img 태그가 있으면 1번째 a 태그의 정보를 사용

        title = news.find("a")[a_idx].get_text().strip()
        link = news.find("a")[href]
        print("{}.{}".format(index+1, title))
        print(" (링크 : {}".format(link))



if __name__ =="__main__":
    # scrape_weather() # 오늘의 날씨 정보 가져오기
    # scrap_headline_news()
    scrape_it_news() #IT 뉴스 정보 가져오기

