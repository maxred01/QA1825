import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://hoster.by/service/domains/")
driver.maximize_window()
driver.find_element(By.ID, 'searchDomain').send_keys('tri-kota')
driver.find_element(By.NAME, 'searchdomainsbutton').click()
time.sleep(5)
assert driver.find_element(By.XPATH, '//div[@class="m-domain-search"]').is_displayed()
print(driver.find_element(By.XPATH, '//span[@class="m-font-s1 text-result"]').text)
assert driver.find_element(By.XPATH, '//span[@class="m-font-s1 text-result"]').text == 'Результаты поис2ка'
time.sleep(1)

# Закрыть браузер
driver.quit()
