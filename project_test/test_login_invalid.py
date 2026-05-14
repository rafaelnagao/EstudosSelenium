import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02LoginInvalid:
    def test_login_invalid(self):
        # Cria o Page Object da tela de login usando o driver vindo da fixture.
        login_page = LoginPage(self.driver)

        # Executa o login com usuário inválido.
        login_page.login("invalid_user", "invalid_password")

        # Valida se a mensagem de erro foi exibida.
        login_page.error_message_displayed()
        assert login_page.get_error_message(login_page.expected_message) == login_page.expected_message
