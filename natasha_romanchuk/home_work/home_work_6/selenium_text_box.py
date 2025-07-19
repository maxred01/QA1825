import selenium

import time
from selenium import webdriver
from selenium .webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@placeholder="Full Name"]').send_keys("Natasha")  # ввод в поле input
driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys("Natasha@mail.com")  # ввод в поле input
driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]').send_keys("Minsk")  # ввод в поле input
driver.find_element(By.XPATH, '(//*[@id="permanentAddress"])[@class="form-control"]').send_keys("Mohilev")  # ввод в поле input
driver.find_element(By.XPATH, '//*[@id="submit"]').click()

element = driver.find_element(By.XPATH,'//*[@style="border: 1px solid rgb(229, 229, 229); margin-top: 50px; padding: 50px;"]')
assert element.is_displayed() == True


time.sleep(3)
driver.quit()

