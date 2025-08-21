import allure
import pytest
from selenium import webdriver


@pytest.fixture()
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    try:
        allure.attach(browser.get_screenshot_as_png(),
                      name=f'screenshot {request.node.name}',
                      attachment_type=allure.attachment_type.PNG)
    except:
        pass

    browser.quit()
