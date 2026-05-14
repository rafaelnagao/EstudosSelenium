import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://demo.applitools.com/')

username = browser.find_element(By.ID, 'username')
checkbox_remember_me = browser.find_element(By.XPATH, "//input[@type='checkbox']")

# is_displayed() - Verifica se um elemento está visível na página
print(username.is_displayed())  # Retorna True se o elemento estiver visível, caso contrário, False
assert username.is_displayed()

# is_enabled() - Verifica se um elemento está habilitado para interação
print(username.is_enabled())  # Retorna True se o elemento estiver habilitado, caso contrário, False
assert username.is_enabled()

# is_selected() - Verifica se um elemento do tipo checkbox ou radio button está selecionado
print(checkbox_remember_me.is_selected())  # Retorna True se o checkbox estiver selecionado, caso contrário, False
assert not checkbox_remember_me.is_selected()  # Verifica se o checkbox não está selecionado
checkbox_remember_me.click()  # Clica no checkbox para selecioná-lo
print(checkbox_remember_me.is_selected())  # Retorna True após clicar no checkbox
assert checkbox_remember_me.is_selected()  # Verifica se o checkbox está selecionado após clicar

time.sleep(5)
browser.quit()

