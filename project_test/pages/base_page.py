from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import TimeoutException


# A classe BasePage é uma abstração que encapsula as operações comuns de interação
# com a página, como encontrar elementos, enviar texto e clicar.
# Ela serve como base para outras classes de página, como LoginPage,
# que herdam essas funcionalidades.
class BasePage:
    def __init__(self, driver):
        # O construtor recebe o driver do Selenium e o armazena como um atributo
        # da classe para ser usado em outros métodos.
        self.driver = driver
        self.action_chains = ActionChains(self.driver)

    def find_element(self, locator):
        # O método find_element recebe um locator (uma tupla que define como localizar
        # um elemento, por exemplo, (By.ID, "username")) e retorna o elemento encontrado.
        self.wait_for_element(locator)

        # O *locator é usado aqui porque find_element espera dois argumentos separados:
        # strategy e value.
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        # O método find_elements é similar ao find_element, mas retorna uma lista
        # de elementos que correspondem ao locator.
        self.wait_for_element(locator)

        # O *locator também é usado aqui porque find_elements espera os argumentos separados.
        return self.driver.find_elements(*locator)

    def send_keys(self, locator, text):
        # O método send_keys envia texto para um campo de entrada.
        # Primeiro garantimos que o elemento esteja presente.
        self.wait_for_element(locator)

        # Depois encontramos o elemento, limpamos o conteúdo antigo
        # e digitamos o novo texto.
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        # O método click é responsável por clicar em um elemento.
        # Primeiro garantimos que ele esteja presente.
        self.wait_for_element(locator)

        # Depois localizamos o elemento e realizamos o clique.
        element = self.find_element(locator)
        element.click()

    def hover(self, locator):
        # O método hover passa o mouse sobre um elemento.
        self.wait_for_element(locator)
        element = self.find_element(locator)
        self.action_chains.move_to_element(element).perform()

    def element_displayed(self, locator):
        # O método element_displayed verifica se um elemento está visível na página.
        # Aqui usamos assert para falhar o teste com mensagem clara, caso não esteja visível.
        assert self.find_element(locator).is_displayed(), (
            f"Elemento com locator {locator} não está visível na página."
        )

    def wait_for_element(self, locator, timeout=10):
        # O método wait_for_element aguarda até que um elemento esteja presente no DOM.
        # IMPORTANTE: Expected Conditions recebe o locator como uma tupla inteira,
        # por isso usamos locator e não *locator.
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def element_exists(self, locator, timeout=5):
        # O método element_exists verifica se um elemento existe na página.
        # Se encontrar dentro do tempo limite, retorna True.
        # Se não encontrar, retorna False.
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def element_not_exists(self, locator, timeout=5):
        # O método element_not_exists verifica se um elemento não existe
        # ou não está presente no DOM dentro do tempo definido.
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return False
        except TimeoutException:
            return True

    def double_click(self, locator):
        # O método double_click realiza um clique duplo em um elemento.
        self.wait_for_element(locator)
        element = self.find_element(locator)
        self.action_chains.double_click(element).perform()

    def right_click(self, locator):
        # O método right_click realiza um clique com o botão direito em um elemento.
        self.wait_for_element(locator)
        element = self.find_element(locator)
        self.action_chains.context_click(element).perform()

    def press_key(self, locator, key):
        # O método press_key envia uma tecla específica para um elemento.
        elem = self.find_element(locator)

        if key == "ENTER":
            elem.send_keys(Keys.ENTER)
        elif key == "SPACE":
            elem.send_keys(Keys.SPACE)
        elif key == "TAB":
            elem.send_keys(Keys.TAB)
        elif key == "ESCAPE":
            elem.send_keys(Keys.ESCAPE)