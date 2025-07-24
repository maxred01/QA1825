import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, '//input[@id="userName"]').send_keys("Polina")
driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("1@gmail.com")
driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys("Minsk")
driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("Postavy")
time.sleep(3)

# driver.execute_script("window.scrollBy(0, 50);")
# driver.find_element(By.XPATH, '//button[@id="submit"]').send_keys(Keys.DOWN)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, '//button[@id="submit"]').click()
time.sleep(3)

elements = driver.find_element(By.XPATH,'//div[@class="border col-md-12 col-sm-12"]')
assert elements.is_displayed() == True
print ('Тест выполнен успешно!')

name_result = driver.find_element(By.ID, 'name')
email_result = driver.find_element(By.ID, 'email')
current_address_result = driver.find_element(By.XPATH, '//p[@id="currentAddress"]')
permanent_address_result = driver.find_element(By.XPATH, '//p[@id="permanentAddress"]')
time.sleep(3)

assert name_result.text.find('Polina') > -1
assert email_result.text.find('1@gmail.com') > -1
assert current_address_result.text.find('Minsk') > -1
assert permanent_address_result.text.find('Postavy') > -1
print ('Тест выполнен успешно!')

time.sleep(3)

# Закрыть браузер
driver.quit()


