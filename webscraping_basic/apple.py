import requests
import re
from bs4 import BeautifulSoup

url ="https://www.apple.com/kr-k12/shop/buy-mac/macbook-air"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

with open("apple.html", "w", encoding="utf8") as f:
    f.write(res.text)

