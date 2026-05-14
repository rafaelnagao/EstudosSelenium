from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(browser, 10)

browser.maximize_window()
browser.get('https://leogcarvalho.github.io/test-automation-practice/')

# Switch to the iframe
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'test-iframe')))

# Wait for the h1 element to be visible and assert it is displayed
h1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Example Domain"]')))
assert h1.is_displayed()

browser.switch_to.default_content() # Volta para o conteudo principal