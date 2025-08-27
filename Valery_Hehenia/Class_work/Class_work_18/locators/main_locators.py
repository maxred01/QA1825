import os
from Valery_Hehenia.Class_work.Class_work_18.page.base_page import WebPage
from Valery_Hehenia.Class_work.Class_work_18.page.elements import WebElement, ManyWebElements


class MainPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.kinopoisk.ru/'

        super().__init__(web_driver, url)

    kinopoisk_home = WebElement(css='[alt="Кинопоиск"]')
    online_kinoteatr = WebElement(css='[target="_self"]:nth-of-type(1)')
    bileti_v_kino = WebElement(css='[target="_self"]:nth-of-type(2)')
    search_kino = WebElement(css='[aria-label="Фильмы, сериалы, персоны"]')
    smotret_kino = WebElement(css='header > button:nth-of-type(4)')
    voiti_button = WebElement(css='button[type="button"]:nth-of-type(3)')
