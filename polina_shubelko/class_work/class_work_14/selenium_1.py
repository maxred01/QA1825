import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://rocketdata.ru/")
driver.maximize_window()
driver.find_element(By.XPATH, '//button[@id="CybotCookiebotDialogBodyButtonAccept"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//a[@href="#popup:feedback"]//a[@aria-haspopup="dialog"]').click()
form_loaded = driver.find_element(By.XPATH, '(//div[@class="tn-atom t-bgimg loaded"])[2]')
assert form_loaded.is_displayed() == True, 'Кнопки "Свяжитесь со мной" нет на экране'

driver.find_element(By.XPATH, '//input[@class="t838__input t-input"]').send_keys("Тарифы")
time.sleep(5)
form_search = driver.find_element(By.XPATH, '(//div[@class="t-site-search-popup t-width t-width_8"])')
assert form_search.is_displayed () == True, 'Открывается вкладка "Тарифы"'

# Закрыть браузер
driver.quit()
