import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login # marca o teste com a tag "login" para facilitar a execução seletiva.
class TestCT01Login:
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        assert self.driver.find_element(By.CLASS_NAME, "title").is_displayed()