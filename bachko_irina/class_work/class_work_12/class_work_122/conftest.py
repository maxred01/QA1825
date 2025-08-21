import time
import pytest
import allure
from selenium import webdriver

import pytest_check as check

@pytest.fixture()
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    # yield browser
    # if hasattr(pytest, 'test_faild') and pytest.test_faild:
    #     try:
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name='скрин экрана',
    #                       attachment_type=allure.attachment_type.PNG
    #                       )
    #     except Exception as e:
    #         print (f'Не удалось сделать скрин' {e})
    yield browser
    if request.node.rep_call.failed:
        try:
            allure.attach(browser.get_screenshot_as_png(),
                          name=f"скрин экрана {request.node.name}",
                          attachment_type=allure.attachment_type.PNG
                          )
        except:
            pass

    browser.quit()