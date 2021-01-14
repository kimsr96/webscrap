from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

url = "https://www.apple.com/kr-k12/shop/bag"
browser.get(url)
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
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="checkout-container"]/div/div[7]/div[1]/div[2]/div/div/div[1]/div/div/div/fieldset/div[1]/div[2]/label/span/span[2]/span').click()


while True:
    time.sleep(3)
    interval = random.randrange(17,23)
    elem = browser.find_element(By.XPATH, '//*[@id="additionalInfo0"]/ul/li[1]/span[2]/span')
    if elem.text == "픽업 불가" or elem.text=="":
        print("픽업 준비중...")
    else:
        print("픽업 가능!!! ")
        browser.maximize_window()
        break
    time.sleep(interval)
    browser.refresh()

# while True:
#     interval = random.randrange(26,34)
#     elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='additionalInfo0']/ul/li[1]/span[2]/span")))

#     if elem.text == "픽업 불가" or elem.text=="":
#         print("픽업 준비중...")
#     else:
#         print("픽업 가능!!! ")
#         break
#     time.sleep(interval)
#     browser.refresh()



# browser.find_element_by_xpath("//*[@id='model-selection']/bundle-selection/store-provider/div[2]/div/div[2]/div/div[1]/div/bundle-selector/div[2]/fieldset/ul/li[3]").click()

# order_url = "https://www.apple.com/kr-k12/shop/bag"
# browser.get(order_url)
# browser.maximize_window()

# browser.find_element(By.LINK_TEXT, '로그인').click()
# browser.find_element(By.NAME, 'appleId').send_keys("kimsr_96@naver.com")
# browser.find_element(By.NAME, 'password').send_keys("Rlatmd96!!.")
# browser.find_element(By.ID, 'signInButtonId').click()
# time.sleep(3)
# browser.find_element(By.XPATH, '//*[@id="shoppingCart.actions.navCheckout"]').click()
# time.sleep(2)
# browser.find_element(By.NAME, 'password').click()
# browser.find_element(By.NAME, 'password').send_keys("Rlatmd96!!.")
# browser.find_element(By.ID, 'signInButtonId').click()