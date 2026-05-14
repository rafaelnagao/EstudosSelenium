import pytest
from selenium import webdriver


# Fixture compartilhada do pytest.
# Ela será executada antes e depois dos testes que usarem "setup_teardown".
@pytest.fixture(scope="class")
def setup_teardown(request):
    # Configura opções do Chrome.
    options = webdriver.ChromeOptions()

    # Desativa recursos que podem atrapalhar a automação com pop-ups.
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    }

    # Aplica as preferências ao navegador.
    options.add_experimental_option("prefs", prefs)

    # Inicia o navegador maximizado e sem extensões.
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")

    # Cria a instância do Chrome.
    driver = webdriver.Chrome(options=options)

    # Espera implícita para ajudar na busca de elementos.
    driver.implicitly_wait(5)

    # Abre a aplicação base do teste.
    driver.get("https://www.saucedemo.com/")

    # Injeta o driver na classe de teste.
    # Por isso, no teste, usamos self.driver.
    request.cls.driver = driver

    # Entrega o fluxo para o teste.
    yield

    # Fecha o navegador ao final do teste.
    driver.quit()