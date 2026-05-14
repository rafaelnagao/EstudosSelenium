import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://saucedemo.com/')

# Localizando o campo de usuário e senha
username = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')
btn_login = browser.find_element(By.ID, 'login-button')

# Preenchendo os campos de usuário e senha
username.send_keys('standard_user')
password.send_keys('secret_sauce')

# Clicando no botão de login
btn_login.click()
time.sleep(2)

# Localizando o título da página
product_title = browser.find_element(By.XPATH, '//span[@class="title"]')
print(product_title.text)
assert product_title.text

# get_attribute() - Obtendo o valor de um atributo
image_backpack = browser.find_element(By.XPATH, '(//img[@class="inventory_item_img"])[1]')
print(image_backpack.get_attribute('alt'))
assert image_backpack.get_attribute('alt') == 'Sauce Labs Backpack'
