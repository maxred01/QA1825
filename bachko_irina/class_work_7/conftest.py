import pytest
from selenium import webdriver
import allure
import time
import pytest_check as check

@pytest.fixture()
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()


    browser.quit()