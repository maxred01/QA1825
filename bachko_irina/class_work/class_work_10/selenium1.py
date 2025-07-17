import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# # Открыть страницу
# driver.get("https://www.google.com")
# # driver.set_window_size(100, 300)
# driver.maximize_window()
# driver.find_element(By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@aria-label="Мне повезёт!"]').click()
#
# # Закрыть браузер
# time.sleep(10) # таймер 5 сек.
# driver.quit()

# Открыть страницу
# driver.get("https://www.spacex.com")
#
# driver.maximize_window()
# driver.find_element(By.XPATH, '(//a[@href="/vehicles/falcon-9/"])[1]').click()
# # driver.find_element(By.XPATH, '(//body[@class="prestige--v4  template-collection"]').click()
# time.sleep(5)
# # img_korjik = driver.find_element(By.XPATH, '(//img[@class="ProductItem__Image Image--fadeIn lazyautosizes Image--lazyLoaded"][1]')
#
# assert img_korjik.is_displayed() == True, ' Картинки нет на экарне'
#
# # Закрыть браузер
# driver.quit()


driver.get("https://shop.spacex.com")
driver.maximize_window()
driver.find_element(By.XPATH,  '//button[@class="Heading Link Link--primary Text--subdued u-h8"]').click()

driver.find_element(By.XPATH, '//input[@id="search-input"]').send_keys('abc')

time.sleep(5)

# Закрыть браузер
driver.quit()