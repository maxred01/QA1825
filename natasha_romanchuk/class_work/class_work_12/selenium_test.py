import selenium

import time
from selenium import webdriver
from selenium .webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
# driver.get("https://emall.by")
# driver.maximize_window()
# driver.find_element(By.XPATH, '//button[@class="btn_btn__jx6SQ btn_btn_colour_black__wifsv btn_btn_size_medium__ugU8B cookies_button__ELP7A"]').click()
# driver.find_element(By.XPATH, '//a[@href="https://emall.by/actions"]').click()
# time.sleep(3)
# img_len = driver.find_element(By.XPATH,'//img[@alt="Первый звонок...для подготовки к учёбе"]')
# assert img_len.is_displayed() == True

driver.get("https://emall.by")
driver.maximize_window()
driver.find_element(By.XPATH, '//button[@class="btn_btn__jx6SQ btn_btn_colour_black__wifsv btn_btn_size_medium__ugU8B cookies_button__ELP7A"]').click()  # согласиться с куки
driver.find_element(By.XPATH, '//input[@class="web_search__input__0oHdp"]').send_keys("бумага")  # ввод в поле input
assert driver.find_element(By.XPATH, '//input[@class="web_search__input__0oHdp"]').text == "туалетная бумага"
time.sleep(3)



