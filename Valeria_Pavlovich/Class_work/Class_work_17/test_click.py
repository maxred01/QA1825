import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Valeria_Pavlovich.Class_work.Class_work_17.locators.locators_button import LocatorsButton


@allure.feature('Elements')
@allure.story('Buttons')
def test_buttons(web_browser):
    with allure.step('Browser start'):
        driver = web_browser
        driver.get('https://demoqa.com/buttons')

    with allure.step('Double click'):
        elements_double_click_btn = driver.find_element(By.ID, LocatorsButton.double_click_btn)
        ActionChains(driver).double_click(elements_double_click_btn).perform()
        time.sleep(2)
        assert driver.find_element(By.ID, LocatorsButton.double_click_message).is_displayed()

    # with allure.step('Right button click'):
    #     elements_right_click_btn = driver.find_element(By.ID, LocatorsButton.right_click_btn)
    #     ActionChains(driver).context_click(elements_right_click_btn).perform()



@allure.feature('Elements')
@allure.story('Upload and download')
def test_upload_download():
    with allure.step('Browser start'):
        driver = webdriver.Chrome()
        driver.get('https://demoqa.com/upload-download')
        driver.maximize_window()

    with allure.step('Upload a file'):
         driver.find_element(By.ID, "uploadFile").sendkeys('D:\\ab.txt')
         time.sleep(2)
