# Assert sempre verifica se o retorno da condicao e true
assert True

# assert numbers
num_esperado = 3
num_obtido = 2
assert num_esperado != num_obtido, f'Esperado {num_esperado} nao e maior que o Atual {num_obtido}'

# assert text
text_esperado = "Selenium Webdriver"
text_obtido = "Selenium Webdriver"
assert text_esperado == text_obtido, f'Esperado {text_esperado}, Atual {text_obtido}.'

# assert text in string
textoesperado = "Seleniumzzzzz"
textoobtido = "Selenium Webdriver"
assert textoesperado not in textoobtido, f"'Esperado '{textoesperado}' dentro da string Atual '{textoobtido}."

# assert is_displayed