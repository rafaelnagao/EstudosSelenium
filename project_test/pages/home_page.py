from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        # Chama a classe pai e entrega o driver para uso nos métodos herdados.
        super().__init__(driver)

        # Locator do título da página de inventário.
        self.title_locator = (By.CLASS_NAME, "title")

        # Locators diretos dos produtos que vamos usar no teste.
        self.backpack_product = (By.ID, "item_4_title_link")
        self.bike_light_product = (By.ID, "item_0_title_link")

        # Botão de adicionar ao carrinho na página de detalhe do produto.
        self.add_to_cart_button = (By.ID, "add-to-cart")

        # Locator do badge do carrinho para verificar a quantidade de itens.
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

        # Locator do ícone do carrinho para clicar e abrir o carrinho.
        self.cart_icon = (By.ID, "shopping_cart_container")

        # Locator para verificar os nomes dos produtos no carrinho.
        self.item_checker = (By.CLASS_NAME, "inventory_item_name")

        # Locator do botão "Continue Shopping" para voltar à listagem de produtos.
        self.continue_shopping_button = (By.ID, "continue-shopping")
        
        # Locators para verificar os detalhes dos produtos na página de detalhe.
        self.item_details_backpack = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
        self.item_details_bike_light = (By.XPATH, "//div[text()='Sauce Labs Bike Light']")

    def inventory_displayed(self):
        # Confirma se o título da lista de produtos está visível.
        return self.find_element(self.title_locator).is_displayed()

    def click_first_product(self):
        # Clica no primeiro produto que vamos testar.
        self.click(self.backpack_product)

    def click_second_product(self):
        # Clica no segundo produto que vamos testar.
        self.click(self.bike_light_product)

    def add_product_to_cart(self):
        # Clica no botão "Add to cart" da página de detalhe.
        self.click(self.add_to_cart_button)

    def cart_badge_count(self):
        # Retorna o número de itens exibidos no badge do carrinho.
        return self.find_element(self.cart_badge).text
    
    def open_cart(self):
        # Clica no ícone do carrinho para abrir o carrinho.
        self.click(self.cart_icon)

    def product_in_cart(self, product_name):
        # Verifica se um produto específico está presente no carrinho.
        items = self.find_elements(self.item_checker)
        return any(item.text == product_name for item in items)
    
    def continue_shopping(self):
        # Clica no botão "Continue Shopping" para voltar à listagem de produtos.
        self.click(self.continue_shopping_button)
    
    def product_details_displayed(self, product_name):
        # Verifica se os detalhes de um produto específico estão visíveis na página de detalhe.
        if product_name == "Sauce Labs Backpack":
            return self.find_element(self.item_details_backpack).is_displayed()
        elif product_name == "Sauce Labs Bike Light":
            return self.find_element(self.item_details_bike_light).is_displayed()
        else:
            raise ValueError(f"Produto '{product_name}' não reconhecido para verificação de detalhes.")
    
