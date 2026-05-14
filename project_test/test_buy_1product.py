import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


# Esta classe usa a fixture "setup_teardown" definida no conftest.py.
@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.checkout_flow # marca o teste com a tag "checkout_flow" para facilitar a execução seletiva.
class TestCT04CheckoutFlow:

    def test_checkout_flow(self):
        # Cria uma espera explícita para elementos críticos da interface.
        wait = WebDriverWait(self.driver, 10)

        # =========================
        # LOGIN
        # =========================

        # Aguarda o campo de username ficar visível e faz login.
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")

        # Valida se entrou na página de inventário.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert self.driver.find_element(By.CLASS_NAME, "title").is_displayed()

        # =========================
        # ADICIONA O PRIMEIRO PRODUTO
        # =========================

        # Abre o detalhe do produto "Sauce Labs Backpack".
        self.driver.find_element(By.ID, "item_4_title_link").click()

        # Aguarda a página de detalhe carregar.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name")))

        # Na página de detalhe do produto, o botão usa o ID genérico "add-to-cart".
        self.driver.find_element(By.ID, "add-to-cart").click()

        # Aguarda o badge do carrinho aparecer.
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))

        # =========================
        # VALIDA O PRIMEIRO PRODUTO NO CARRINHO
        # =========================

        # Vai para o carrinho.
        self.driver.find_element(By.ID, "shopping_cart_container").click()

        # Aguarda pelo menos um item aparecer no carrinho.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

        # Confirma que o Backpack está presente.
        assert "Sauce Labs Backpack" in self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

        # =========================
        # ADICIONA O SEGUNDO PRODUTO
        # =========================

        # Volta para a listagem de produtos.
        self.driver.find_element(By.ID, "continue-shopping").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

        # Abre o detalhe do produto "Sauce Labs Bike Light".
        self.driver.find_element(By.ID, "item_0_title_link").click()

        # Aguarda a página de detalhe do segundo produto carregar.
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_details_name.large_size")))

        # Na página de detalhe, o botão continua sendo o ID genérico "add-to-cart".
        self.driver.find_element(By.ID, "add-to-cart").click()

        # Valida se o badge do carrinho mostra 2 itens.
        badge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
        assert badge.text == "2"

        # =========================
        # VALIDA OS DOIS PRODUTOS NO CARRINHO
        # =========================

        # Vai novamente para o carrinho.
        self.driver.find_element(By.ID, "shopping_cart_container").click()

        # Aguarda os itens ficarem visíveis.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

        # Busca todos os nomes de produtos exibidos no carrinho.
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # Confirma que os dois produtos estão presentes.
        assert any("Sauce Labs Backpack" in el.text for el in cart_items)
        assert any("Sauce Labs Bike Light" in el.text for el in cart_items)

        # =========================
        # REMOVE O PRIMEIRO PRODUTO
        # =========================

        # Remove o Backpack do carrinho.
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        # Aguarda o item removido desaparecer da tela.
        wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]")
            )
        )

        # Busca novamente os itens restantes do carrinho.
        remaining_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

        # Confirma que o Bike Light ainda está no carrinho.
        assert any("Sauce Labs Bike Light" in el.text for el in remaining_items)

        # =========================
        # CHECKOUT
        # =========================

        # Clica no botão de checkout.
        self.driver.find_element(By.ID, "checkout").click()

        # Aguarda a tela de informações do checkout.
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
        assert "Checkout: Your Information" in self.driver.find_element(By.CSS_SELECTOR, ".title").text

        # Preenche os dados do cliente.
        self.driver.find_element(By.ID, "first-name").send_keys("Rafael")
        self.driver.find_element(By.ID, "last-name").send_keys("Nagao")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")

        # Continua para o overview.
        self.driver.find_element(By.ID, "continue").click()

        # Aguarda a tela de resumo do checkout.
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
        assert "Checkout: Overview" in self.driver.find_element(By.CSS_SELECTOR, ".title").text

        # =========================
        # FINALIZA A COMPRA
        # =========================

        # Finaliza o pedido.
        self.driver.find_element(By.ID, "finish").click()

        # Aguarda a mensagem final de sucesso.
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".complete-header")))

        # Valida se a mensagem final está visível.
        complete_header = self.driver.find_element(By.CSS_SELECTOR, ".complete-header")
        assert complete_header.is_displayed()
        assert "THANK YOU" in complete_header.text.upper()
        self.driver.save_screenshot("./screenshots/test_checkout_flow_success.png") # salva um screenshot do resultado final para evidência.