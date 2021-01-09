from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome("/Users/alvin/Desktop/coding/webscrap/chromedriver")
browser.maximize_window()

url = "https://www.daum.net"
browser.get(url)

elem = browser.find_element_by_class_name("inner_search").click()

input = browser.find_element_by_id("q")
input.send_keys("송파 헬리오시티")
input.send_keys(Keys.RETURN)

soup = BeautifulSoup(browser.page_source, "lxml")

# hauses = soup.find_all("tr")
# for idx, hause in enumerate(hauses):
#     if hause==hauses[0]:
#         continue
#     print(f"=========매물{idx}==========")
#     info = hauses[idx].get_text().split()
#     for idx, eachif in enumerate(info):
#         if idx == 0:
#             print(f"거래 : {info[idx]}")
#         elif idx == 1:
#             print(f"면적 : {info[idx]}")
#         elif idx == 2:
#             print(f"가격 : {info[idx]}")
#         elif idx == 3:
#             print(f"동 : {info[idx]}")
#         elif idx == 4:
#             print(f"층 : {info[idx]}")
#Solution
# data_rows = table=soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
# for index, row in enumerate(data_rows):
#         columns = row.find_all("td")

#         print("======== 매물 {} ==========" .format(index+1))
#         print("거래: ", columns[0].get_text().strip())
#         print("면적: ", columns[1].get_text().strip())
#         print("가격: ", columns[2].get_text().strip())
#         print("동: ", columns[3].get_text().strip())
#         print("층: ", columns[4].get_text().strip())


hauses = soup.find_all("tr")
for idx, hause in enumerate(hauses):
    columns = hause.find_all("td")
    if hause==hauses[0]:
        continue
    print("======== 매물 {} ==========" .format(idx+1))
    print("거래: ", columns[0].get_text().strip())
    print("면적: ", columns[1].get_text().strip())
    print("가격: ", columns[2].get_text().strip())
    print("동: ", columns[3].get_text().strip())
    print("층: ", columns[4].get_text().strip())
         