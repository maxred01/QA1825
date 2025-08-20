import pytest
from selenium import webdriver
import time
import requests
import allure
import pytest_check as check

@pytest.fixture
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    if request.node.rep_call.failed:
        try:
            allure.attach(browser.get_screenshot_as_png(),
                          name='Скрин экрана',
                          attachment_type=allure.attachment_type.PNG
                          )
        except Exception as e:
            print(f'Не удалось сделать скриншот {e}')
    browser.quit()



