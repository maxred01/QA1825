from selenium import webdriver
import time
from selenium.webdriver.common.by import By


full_name = 'Peter Parket'
email = 'test@test.com'
current_address = 'г. Минск'
permanent_address = 'г. Ивацевичи'

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '[placeholder="Full Name"]').send_keys(full_name)
driver.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '[placeholder="Current Address"]').send_keys(current_address)
driver.find_element(By.CSS_SELECTOR, '[id="permanentAddress"]').send_keys(permanent_address)

driver.find_element(By.CSS_SELECTOR, '[id="submit"]').click()

time.sleep(1)


elements = driver.find_elements(By.XPATH, "//p[@class='mb-1']")
for el in elements:
     print(el.text)

assert elements[0].text == f'Name:{full_name}'
assert elements[1].text == f'Email:{email}'
assert elements[2].text == f'Current Address :{current_address}'
assert elements[3].text == f'Permananet Address :{permanent_address}'
driver.quit()