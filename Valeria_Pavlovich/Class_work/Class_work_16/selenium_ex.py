import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# # Открыть страницу
# driver.get("https://www.google.com")
#
# # Закрыть браузер
# driver.quit()

driver.get("https://hotels.belavia.by/?sid=2662c0f7-28d9-4fe7-a052-c5b7ea3b77ee")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@data-testid="search-button"]').click()
driver.find_element(By.XPATH, '//*[@data-testid="destination-input"]').send_keys('Москва')
driver.find_element(By.XPATH, '//*[@data-testid="search-button"]').click()
time.sleep(7)
assert driver.find_element(By.XPATH,"//*[contains(concat(' ', normalize-space(@class), ' '), ' zenregioninfo ')][1]").is_displayed()
print(driver.find_element(By.XPATH,"//*[contains(concat(' ', normalize-space(@class), ' '), ' zenregioninfo ')][1]").text)
assert driver.find_element(By.XPATH,"//*[contains(concat(' ', normalize-space(@class), ' '), ' zenregioninfo ')][1]").text == 'Москва, Россия'
time.sleep(1)
# popup = driver.find_element(By.XPATH, "//label[@class='Input-module__label--1p3o1 Input-module__label_size_m--PyZym']")
# assert popup.is_displayed() == True, 'На странице есть выпадающий список с городами'
# driver.quit()

