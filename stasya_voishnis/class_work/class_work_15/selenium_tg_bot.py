import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://www.royal.uk/")
time.sleep(5)
driver.maximize_window() # максимальное разрешение экрана
driver.find_element(By.XPATH, '//button [@id="CybotCookiebotDialogBodyButtonDecline"]').click()
driver.find_element(By.XPATH, '(//a [@href="https://www.royal.uk/the-king-0"])[1]').click()
time.sleep(1)
h1_king = driver.find_element(By.XPATH, '//h1[@class="page-title"]')

assert h1_king.is_displayed() == True, ' The King не на экране'

driver.find_element(By.XPATH, '//button[@class="search__toggle"]').click()
driver.find_element(By.XPATH, '//input[@class="search__input form-text"]').send_keys('The-king')
driver.find_element(By.XPATH, '//*[@name="op"]').click()
time.sleep(5)

assert driver.find_element(By.XPATH, '//h2[@class="infinity-grid-section__title"]').is_displayed()
print(driver.find_element(By.XPATH, '//h2[@class="infinity-grid-section__title"]').text)
assert driver.find_element(By.XPATH, '//h2[@class="infinity-grid-section__title"]').text == 'Search: The-king'

# Закрыть браузер
time.sleep(5)
driver.quit()