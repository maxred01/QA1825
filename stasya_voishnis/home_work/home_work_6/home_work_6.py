import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@placeholder="Full Name"]').send_keys('Kira Yukimura')
driver.find_element(By.XPATH, '//*[@placeholder="name@example.com"]').send_keys('kira.fox@gmail.com')
driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]').send_keys('Japan')
driver.find_element(By.XPATH, '//*[@id="permanentAddress"]').send_keys('Beacon Hills')
driver.find_element(By.XPATH, '//form//button').click()

element = driver.find_element(By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), ' border ')]")
assert element.is_displayed() == True


time.sleep(5)
driver.quit()

