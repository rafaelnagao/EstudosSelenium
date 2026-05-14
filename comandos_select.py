import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://leogcarvalho.github.io/test-automation-practice/')

dropdown_options = Select(browser.find_element(By.XPATH, '//select[@id="dropdown"]'))
dropdown_options.select_by_visible_text('Option 2') # select by text
time.sleep(3)

dropdown_options.select_by_value('option3') # select by value
time.sleep(3)

dropdown_options.select_by_index(0) # select by index
time.sleep(3)
