import requests
import re
from bs4 import BeautifulSoup

url ="https://www.coupang.com/np/search?src=1139086&spec=10799999&addtag=900&ctag=HOME&lptag=AF8824652&itime=20210105152208&pageType=HOME&pageValue=HOME&wPcid=15804024795931296439540&wRef=click.linkprice.com&wTime=20210105152208&redirect=landing&traceid=V0-189-0000000000000000&subid=A100662972&subparam=v0304000091090b8259ffff39417f8d7cb29921fe71fe%7C2683046250DM1N%7C9999%7C3%7C0&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
print(res.text) 