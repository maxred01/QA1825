import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://www.hoyolab.com/home")
driver.maximize_window()
time.sleep(20)
#driver.find_element(By.XPATH, '//button[@aria-label="close"]').click()
#driver.find_element(By.XPATH,'//button[@class="hyl-button mhy-interest-selector__copy normal__primary hyl-button__lg hyl-button-loading__lg"]').click()
#driver.find_element(By.XPATH, '//div[@class="login-box-side_bottom__btn pointer"]').click()
driver.find_element(By.XPATH, '//label[@class="mhy-autocomplete__label"]').send_keys('Фаэнон')
driver.find_element(By.XPATH,'//div[@data-route-name="search-id"]').click()
time.sleep(5)
#assert driver.find_element(By.XPATH, '//div[@class="mhy-search-page__result" ]').is_displayed()
#print(driver.find_element(By.XPATH,'//div[@data-index = "4"]').text)
driver.quit()
