from selenium import webdriver

browser = webdriver.Chrome("../chromedriver.exe")
browser.get("https://www.apple.com/kr-k12/shop/buy-mac/macbook-air")
elem = browser.find_element_by_xpath("//*[@id='configuration-form']/div/span/button")
elem.click()


