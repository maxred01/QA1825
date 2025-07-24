import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://trikota.tv/")
driver.maximize_window() # максимальное разрешение экрана
driver.find_element(By.XPATH, '//div [@class="header__menu"] //a[@title="О мультсериале"]').click()
driver.find_element(By.XPATH, '(//div[@class="character-section__next"])[1]').click()
time.sleep(1)
# img_korjik = driver.find_element(By.XPATH, '(//img[@src="/upload/iblock/cbf/cbf1e9ed2785c66c903e794c95e738b7.png"])[1]')
#
# assert img_korjik.is_displayed() == True, ' Картинки коржика нет на экарне'


# Закрыть браузер
time.sleep(10)
driver.quit()

