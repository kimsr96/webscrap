import requests
import re
from bs4 import BeautifulSoup

url ="https://www.coupang.com/np/search?src=1139086&spec=10799999&addtag=900&ctag=HOME&lptag=AF8824652&itime=20210105152208&pageType=HOME&pageValue=HOME&wPcid=15804024795931296439540&wRef=click.linkprice.com&wTime=20210105152208&redirect=landing&traceid=V0-189-0000000000000000&subid=A100662972&subparam=v0304000091090b8259ffff39417f8d7cb29921fe71fe%7C2683046250DM1N%7C9999%7C3%7C0&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(res.text) 

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(item[1].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("  <광고 상품 제외합니다> ")
    name = item.find("div", attrs={"class":"name"}).get_text()

    #애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("  <평점 없는 상품 제외합니다> ")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print("  <평점 없는 상품 제외합니다> ")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100: 
        print(name, price, rate, rate_cnt)