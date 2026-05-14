import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

# title - Retorna o título da página
print('O título da página é:', browser.title)

# current_url - Retorna a URL atual da página
print('A URL atual da página é:', browser.current_url)

# page_source - Retorna o código-fonte da página
print('O código-fonte da página é:', browser.page_source)

# window_handles - Retorna uma lista de identificadores de janelas abertas
print('As janelas abertas são:', browser.window_handles)

# name - Retorna o nome do navegador
print('O nome do navegador é:', browser.name)
