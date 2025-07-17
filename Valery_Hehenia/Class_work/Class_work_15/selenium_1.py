from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://ru.riki.team/brands/fiksiki/")
driver.maximize_window()
driver.find_element(By.XPATH, '//i[contains(@class, "search_open") and contains(@class, "js_search_open")]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//input[@type="search" and @placeholder="Что вы хотите найти?"]').send_keys('Смешарики')
time.sleep(2)
driver.find_element(By.XPATH, '//button[@class="btn_search"]').click()

time.sleep(5)
# driver.find_element(By.XPATH, '//li[contains(@class, "js_parent_menu_item") and .//a[contains(text(), "Бренды")]]').click()
# driver.find_element(By.XPATH, '//a[@class="brand_item_inner js_item_hov"]//img[@src="/upload/iblock/e2f/66zh48skvj9bvofqxmc4rh3xuzqz43oy.png"]').click()

# peremennaya = driver.find_element(By.XPATH, '//div[@class="banner_bg"]')

#
# assert peremennaya.is_displayed() == True
# assert text.is_displayed() == True

driver.quit()


# driver = webdriver.Chrome()
# driver.get("https://github.com/")
# driver.set_window_size(1600, 900)
# driver.quit()
#
# driver = webdriver.Chrome()
# driver.get("https://rabota.by/")
# driver.maximize_window()
# time.sleep(10)
#driver.quit()