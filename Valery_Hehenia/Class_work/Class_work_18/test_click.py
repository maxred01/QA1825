from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import LabelType
from allure_commons.types import Severity

import pytest_check as check
from Valery_Hehenia.Class_work.conftest import web_browser
from Valery_Hehenia.Class_work.Class_work_18.locators.locators import LocatorsButton



@allure.feature("Раздел Elements")
@allure.story("Вкладка Buttons")
def test_demoqa_button(web_browser):


     with allure.step(f'Запуск и настройка сайта'):
          driver = web_browser
          driver.get("https://demoqa.com/buttons")


     with allure.step(f'Двойной клик'):
          elements_double_click_btn = driver.find_element(By.ID, LocatorsButton.double_click_btn)
          ActionChains(driver).double_click(elements_double_click_btn).perform()

     with allure.step(f'Проверка двойного клика'):
          message_double = driver.find_element(By.ID, LocatorsButton.double_click_btn_message)
          assert message_double.is_displayed()
     time.sleep(0.5)


     with allure.step(f'Клик ПКМ'):
          elements_right_click_btn = driver.find_element(By.ID, LocatorsButton.right_click_btn)
          ActionChains(driver).context_click(elements_right_click_btn).perform()

     with allure.step(f'Проверка нажатия ПКМ'):
          message_right = driver.find_element(By.ID, LocatorsButton.right_click_btn_message)
          assert message_right.is_displayed()
     time.sleep(0.5)



     # with allure.step(f'Одиночный клик'):
     #      driver.find_elements(By.CSS_SELECTOR, LocatorsButton.left_click_btn[3]).click()
     # with allure.step(f'Проверка нажатия ЛКМ'):
     #      message_left = driver.find_element(By.ID, 'dynamicClickMessage')
     #      assert message_left.is_displayed()
     # time.sleep(0.5)




# @allure.feature("Раздел Elements")
# @allure.story("Вкладка Upload")
# def test_demoqa_button_upload(web_browser):
#
#      with allure.step(f'Запуск и настройка сайта'):
#           driver = web_browser
#           driver.get("https://demoqa.com/upload-download")
#
#
#
#      with allure.step(f'Проверка выбора файла для загрузки'):
#           driver.find_element(By.TAG_NAME, 'INPUT').send_keys('D:\\Studies\\Python\\test.txt')
#      time.sleep(2)





