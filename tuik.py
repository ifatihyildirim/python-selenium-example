import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/isafatihyildirim/Documents/Dev/tuik/chromedriver')
driver.get('http://tuik.gov.tr/UstMenu.do?metod=temelist')

links = driver.find_elements_by_class_name('link2')
# print(links)
for link in links:
    print(link.get_attribute("href"))

driver.quit()