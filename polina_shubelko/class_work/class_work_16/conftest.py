import time
import pytest
import allure
from selenium import webdriver
import pytest_check as check
from QA1825.polina_shubelko.class_work.class_work_16.page.base_page import WebPage

@pytest.fixture
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    try:
        allure.attach(browser.get_screenshot_as_png(),
                      name = f"скрин {request.node.name}",
                      attachment_type = allure.attachment_type.PNG)
    except:
        pass


    browser.quit()
