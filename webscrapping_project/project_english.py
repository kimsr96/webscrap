import requests
from bs4 import BeautifulSoup

url ="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

eng = soup.find_all("div",attrs={"class":"conv_txt"})[1].find_all("b")
kor = soup.find_all("div",attrs={"class":"conv_txt"})[0].find_all("b")

for i in eng:
    print(i.get_text())
for y in kor:
    print(y.get_text())
    