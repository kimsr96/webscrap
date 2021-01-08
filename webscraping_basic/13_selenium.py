 # -*- coding: utf-8 -*- 
from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/alvin/Desktop/coding/webscrap/webscraping_basic/chromedriver")

#1 네아버 이동
browser.get("http://naver.com")


#2 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3 id,pw 입력
browser.find_element_by_id("id").send_keys("kimsr960")
browser.find_element_by_id("pw").send_keys("rlatmd96!!.")

time.sleep(3)

#4 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

#5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
#browser.close()
browser.quit()