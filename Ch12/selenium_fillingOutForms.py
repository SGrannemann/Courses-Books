from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://login.metafilter.com')
# use whatever find methods gets you to the part of the form you want to fill out.
userElem = browser.find_elements_by_id('user_name')
userElem.send_keys('your user name here')

passwordElem = browser.find_elements_by_id('user_pass')
passwordElem.send_keys('your password here')
#submit works on any field of the form
passwordElem.submit()