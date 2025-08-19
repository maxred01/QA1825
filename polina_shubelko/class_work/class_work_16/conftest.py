import time
import pytest
import allure
from selenium import webdriver
import pytest_check as check

@pytest.fixture
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    if request.node.rep_call.failed:
        try:
            allure.attach(browser.get_screenshot_as_png(),
                          name = f'скрин экрана {request.node.name}',
                          attachment_type = allure.attachment_type.PNG)
        except:
            pass




    browser.quit()
