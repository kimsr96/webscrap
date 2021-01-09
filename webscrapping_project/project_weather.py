import requests
from bs4 import BeautifulSoup

url1 ="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
res1 = requests.get(url1)
res1.raise_for_status()
soup1 = BeautifulSoup(res1.text,"lxml")

today_whether = soup1.find("p", attrs={"class":"cast_txt"})
print("[오늘의 날씨]") 
print(today_whether.get_text())
today_temp = soup1.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
print(f"현재{today_temp}")


# rain_morn = soup1.find("span", attrs={"class":"point_time morning"}).get_text().split()
# rain_afternoon = soup1.find("span", attrs={"class":"point_time afternoon"}).get_text().split()
# print(f"오전 {rain_morn} / 오후 {rain_afternoon}")


rain = soup1.find("li", attrs={"class":"date_info today"})
rain_info = rain.find_all("span", attrs={"class":"rain_rate"})
print("오전"+rain_info[0].get_text()+"/ 오후" + rain_info[1].get_text())



dust = soup1.find("dl", attrs={"class":"indicator"})
smallDust = dust.find_all("dt")
dustAmount = dust.find_all("dd")
for i in range(0,2):
    print(smallDust[i].get_text()+":"+ dustAmount[i].get_text())

# [오늘의 날씨]
# 흐림, 어제보다 00도 높아요
# 현재 00도C (최저00/ 최고00)
# 오전 강수확률 00% / 오후 강수확률 00%
# 미세먼지 00좋음
# 초미세먼지 00 좋은