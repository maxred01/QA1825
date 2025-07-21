import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@id="userName"]').send_keys("Polina")
time.sleep(3)
driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("1@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys("Minsk")
time.sleep(3)
driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("Postavy")
time.sleep(3)

driver.find_element(By.XPATH, '//button[@id="submit"]').click()

time.sleep(3)

elements = driver.find_element(By.XPATH,'//div[@class="border col-md-12 col-sm-12"]')
assert elements.is_displayed() == True
print ('Тест выполнен успешно!')

time.sleep(3)

# Закрыть браузер
driver.quit()
