from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# O método login é responsável por realizar o fluxo de login, e pode ser reutilizado em outros testes que precisem autenticar.
class LoginPage(BasePage):
    def __init__(self, driver):
        # Chama o construtor da classe pai e entrega o driver.
        super().__init__(driver)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

        self.expected_message = "Epic sadface: Username and password do not match any user in this service"

    def login(self, username, password):
        # Preenche o usuário.
        self.send_keys(self.username_input, username)

        # Preenche a senha.
        self.send_keys(self.password_input, password)

        # Clica no botão de login.
        self.click(self.login_button)

    def error_message_displayed(self):
        # Valida se a mensagem de erro está visível na tela.
        assert self.driver.find_element(By.XPATH, "//h3[@data-test='error']").is_displayed()
    
    def get_error_message(self, expected_message):
        # Recupera o texto da mensagem de erro e compara com a mensagem esperada.
        actual_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert actual_message == expected_message, f"Expected: {expected_message}, Actual: {actual_message}"
        return actual_message