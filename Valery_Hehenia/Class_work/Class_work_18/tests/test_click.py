import time
import allure

from Valery_Hehenia.Class_work.Class_work_18.locators.locators import ButtonPage
# from Valery_Hehenia.Class_work.conftest import web_browser




@allure.feature("Раздел Elements")
@allure.story("Вкладка Buttons")
def test_buttons(web_browser):
     with allure.step(f'Запуск и настройка сайта'):
          driver = ButtonPage(web_browser)
          # driver.get("https://demoqa.com/buttons")


     with allure.step(f'Двойной клик'):
          driver.double_click_btn.double_click()
          time.sleep(0.5)
          assert not driver.double_click_btn_message.is_visible()


     # with allure.step(f'Проверка двойного клика'):



     with allure.step(f'Клик ПКМ'):
          driver.right_click_btn.right_mouse_click()
          time.sleep(0.5)
          assert driver.right_click_btn_message.is_visible()

     #
     # with allure.step(f'Проверка нажатия ПКМ'):
     #      message_right = driver.find_element(By.ID, LocatorsButton.right_click_btn_message)
     #      assert message_right.is_displayed()
     # time.sleep(0.5)



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





