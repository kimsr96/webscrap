from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

url = "https://www.apple.com/kr-k12/shop/buy-mac/macbook-air"
browser.get(url)


while True:
    color = browser.find_element(By.XPATH, '//*[@id="model-selection"]/bundle-selection/store-provider/div[2]/div/div[2]/div/div[1]/div/bundle-selector/div[2]/fieldset/ul/li[3]').click()
    interval = random.randrange(26,34)
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='model-selection']/bundle-selection/store-provider/div[2]/div/div[2]/div/div[1]/div/bundle-selector/div[3]/div[1]/div/ul[2]/li[2]/div/div/div/div/div/span[2]")))

    if elem.text == "현재 Apple 가로수길에서 이용할 수 없음" or elem.text=="":
        print("픽업 준비중...")
    else:
        print("픽업 가능!!! ")
        break
    time.sleep(interval)
    browser.refresh()



browser.find_element_by_xpath("//*[@id='model-selection']/bundle-selection/store-provider/div[2]/div/div[2]/div/div[1]/div/bundle-selector/div[2]/fieldset/ul/li[3]").click()

order_url = "https://www.apple.com/kr-k12/shop/bag"
browser.get(order_url)
browser.maximize_window()

browser.find_element(By.LINK_TEXT, '로그인').click()
browser.find_element(By.NAME, 'appleId').send_keys("kimsr_96@naver.com")
browser.find_element(By.NAME, 'password').send_keys("Rlatmd96!!.")
browser.find_element(By.ID, 'signInButtonId').click()
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="shoppingCart.actions.navCheckout"]').click()
time.sleep(2)
browser.find_element(By.NAME, 'password').click()
browser.find_element(By.NAME, 'password').send_keys("Rlatmd96!!.")
browser.find_element(By.ID, 'signInButtonId').click()