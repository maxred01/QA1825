import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, '//input[@class=" mr-sm-2 form-control"]').send_keys('nastya')
time.sleep(5)
driver.find_element(By.ID, 'userEmail').send_keys('test01@gmail.com')
time.sleep(5)
driver.find_element(By.ID,'currentAddress').send_keys('г. Минск, ул. Победителей, д. 1')
time.sleep(5)
driver.find_element(By.ID,'permanentAddress').send_keys('г. Минск, ул. Победителей, д. 1')
time.sleep(5)
driver.find_element(By.XPATH,'//button[@class="btn btn-primary"]').click()
time.sleep(10)
output = driver.find_element(By.XPATH,'//div[@class="border col-md-12 col-sm-12"]')
assert output.is_displayed()
print("Тест пройден успешно!")
driver.quit()