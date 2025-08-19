import pytest
from selenium import webdriver
import allure
import time
import pytest_check as check
@pytest.fixture()
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    # if hasattr(pytest, 'test_failed') and pytest.test_failed:
    #     try:
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name="screenshot",
    #                       attachment_type=allure.attachment_type.PNG
    #                       )
    #     except Exception as e:
    #         print(f'Screenshot failed {e}')
    if request.node.rep_call.failed:
        try:
            allure.attach(browser.get_screenshot_as_png(),
                          name=f'screenshot {request.node.name}',
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass


    browser.quit()
