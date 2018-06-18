from selenium import webdriver
from selenium.webdriver.common import keys

userName   =
passWord   = 

driver = webdriver.Chrome()
driver.get("https://acorn.utoronto.ca/")

#action section
#login section
#login elements
userNameInput = driver.find_element_by_id('username')
passWordInput = driver.find_element_by_id('password')
loginButton   = driver.find_element_by_name('_eventId_proceed')

driver.implicitly_wait(40)

#login action
userNameInput.clear()
userNameInput.send_keys(userName)
passWordInput.clear()
passWordInput.send_keys(passWord)
loginButton.click()

driver.implicitly_wait(20)

#search course section
enrolManager  = driver.find_element_by_class_name('icon-right-dir')
enrolManager.click()

driver.implicitly_wait(10)

# courseButtons = driver.find_element_by_xpath('//a[@href="'+'#/courses/0'+'"]')
courseButtons = driver.find_element_by_xpath("//*[contains(text(), 'Courses')]")
courseButtons.click()

driver.implicitly_wait(2)
#course input
# courseInput = driver.find_element_by_id('typeaheadInput')
enrolButtons = driver.find_element_by_xpath("//span[contains(text(), 'Enrol')]")
enrolButtons.click()
