from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://nostarch.com')
# the html tag is the root tag and therefore usually a safe anchor for doing stuff on the whole site
htmlElem = browser.find_elements_by_tag_name('html')
htmlElem.send_keys(Keys.END)
htmlElem.send_keys(Keys.HOME)