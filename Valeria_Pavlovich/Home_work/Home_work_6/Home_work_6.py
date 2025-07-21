import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="userName-wrapper"]//input').send_keys('Alice')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="userEmail-wrapper"]//input').send_keys('rabbit@forest.com')
time.sleep(1)
driver.find_element(By.XPATH, '''//*[@id="currentAddress-wrapper"]//*[local-name() = 'textarea']''').send_keys('Oxford')
time.sleep(1)
driver.find_element(By.XPATH, '''//*[@id="permanentAddress-wrapper"]//*[local-name() = 'textarea']''').send_keys('Wonderland')
time.sleep(1)
submit_btn = driver.find_element(By.XPATH, '//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()
time.sleep(2)

output = driver.find_element(By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), ' border ')]")
assert output.is_displayed() == True, 'The information entered in the fields is shown'
assert driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="name"]').text == 'Name:Alice'
assert driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="email"]').text == 'Email:rabbit@forest.com'
assert driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="currentAddress"]').text == 'Current Address :Oxford'
assert driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="permanentAddress"]').text == 'Permananet Address :Wonderland'
print(driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="name"]').text)
print(driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="email"]').text)
print(driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="currentAddress"]').text)
print(driver.find_element(By.XPATH,'//*[@id="output"]//*[@id="permanentAddress"]').text)