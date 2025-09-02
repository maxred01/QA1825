import allure
import pytest
from selenium import webdriver


@pytest.fixture
def web_browser(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser
    if request.node.rep_call.failed:
        try:
            allure.attach(browser.get_screenshot_as_png(),
                                                name='скрин экрана',
                                                atachment_type=allure.attachment_type.PNG)
        except:
            pass

    # if hasattr(pytest, 'test_faild') and pytest.test_faild:
    #     try:
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name='скрин экрана',
    #                       atachment_type=allure.attachment_type.PNG
    #                       )
    #     except Exception as e:
    #         print(f'Не удалось сделать скрин{e}')



    browser.quit()