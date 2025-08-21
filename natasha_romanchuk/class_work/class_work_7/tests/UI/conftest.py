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

    # Если тест упал → сделаем скриншот
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Скрин экрана",
            attachment_type=allure.attachment_type.PNG
        )


    browser.quit()


