import time
from selenium import webdriver

browser = webdriver.Chrome()

# get() - Acessa a URL informada
browser.get('https://www.saucedemo.com/')
time.sleep(5)

# maximize_window() - Maximiza a janela do navegador
browser.maximize_window()
time.sleep(5)

# refresh() - Atualiza a página
browser.refresh()

# back() - Volta para a página anterior
browser.back()

# forward() - Avança para a próxima página
browser.forward()

# close() - Fecha uma aba do navegador
browser.close()

# quit() - Encerra o processo do navegador
browser.quit()
