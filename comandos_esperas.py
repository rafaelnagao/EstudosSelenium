from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://leogcarvalho.github.io/test-automation-practice/')

wait = WebDriverWait(browser, 15)

button = wait.until(EC.element_to_be_clickable((By.ID, 'delayed-button'))).click()

dly_message = wait.until(EC.visibility_of_element_located((By.ID, 'delayed-message')))
target_message = browser.find_element(By.ID, 'delayed-message').text
assert target_message == "This is the delayed message!"
print('A frase apareceu!')
