import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

# find_element() - Retorna o primeiro elemento que corresponde ao critério de busca
username = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')
print('O elemento encontrado é:', username)
print('O elemento encontrado é:', password)

#send_keys() - Envia texto para um elemento
username.send_keys('standard_user')
password.send_keys('secret_sauce')

time.sleep(5)

# find_elements() - Retorna uma lista de elementos que correspondem ao critério de busca
auth_fields = browser.find_elements(By.XPATH, '//*[@class="input_error form_input"]')
print(auth_fields)
print(len(auth_fields))

browser.quit()