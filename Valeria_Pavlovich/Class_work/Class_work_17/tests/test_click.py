import time
import allure
from Valeria_Pavlovich.Class_work.Class_work_17.locators.main_locators import MainPage


@allure.feature('Elements')
@allure.story('Buttons')
def test_buttons(web_browser):
    with allure.step('Browser start'):
        driver = MainPage(web_browser)

    elements = [
        ('Belavia logo', driver.belavia_logo),
        ('Ostrovok logo', driver.ostrovok_logo),
        ('Language widget', driver.language_widget),
        ('Currency widget', driver.currency_widget),
        ('Feedback form button', driver.feedback_form),
        ('Sign in button', driver.sign_in_button)
        ('Menu button', driver.menu_button)
    ]
    for name, element in elements:
        with allure.step(f'{name} is displayed'):
            time.sleep(2)
            assert element.is_visible()
