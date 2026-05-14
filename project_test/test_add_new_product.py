import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.home_page import HomePage


# usefixtures diz ao pytest para executar a fixture "setup_teardown"
# antes e depois dos testes desta classe
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.add_product  # Marca o teste para execução seletiva.
class TestCT03AddProduct:
    def test_add_product(self):
        # Cria uma espera explícita de até 10 segundos.
        # Isso é útil para esperar elementos aparecerem ou ficarem clicáveis.
        wait = WebDriverWait(self.driver, 10)

        # Faz login no sistema.
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # Valida se a página de inventário foi carregada com sucesso.
        home_page = HomePage(self.driver)
        assert home_page.inventory_displayed()

        # Entra no detalhe do primeiro produto.
        home_page.click_first_product()

        # Confirma se a página de detalhe do produto abriu.
        assert home_page.product_details_displayed("Sauce Labs Backpack")

        # Adiciona o primeiro produto ao carrinho.
        home_page.add_product_to_cart()

        # Verifica se o badge do carrinho mostra 1 item.
        assert home_page.cart_badge_count() == "1"

        # Abre o carrinho.
        home_page.open_cart()

        # Confirma se o primeiro produto está no carrinho.
        assert home_page.product_in_cart("Sauce Labs Backpack")

        # Clica em "Continue Shopping" para voltar à listagem de produtos.
        home_page.continue_shopping()

        # Confirma se voltou para a página de inventário.
        assert home_page.inventory_displayed()

        # Abre o detalhe do segundo produto.
        home_page.click_second_product()

        # Confirma se o detalhe do segundo produto foi carregado.
        assert home_page.product_details_displayed("Sauce Labs Bike Light")

        # Adiciona o segundo produto ao carrinho.
        home_page.add_product_to_cart()

        # Verifica se o carrinho agora mostra 2 itens.
        assert home_page.cart_badge_count() == "2"

        # Abre novamente o carrinho.
        home_page.open_cart()

        # Confirma se os dois produtos estão presentes no carrinho.
        assert home_page.product_in_cart("Sauce Labs Backpack")
        assert home_page.product_in_cart("Sauce Labs Bike Light")