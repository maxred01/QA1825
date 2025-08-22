import time
import requests
from termcolor import colored

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPage(object):
    _web_driver = None

    def __init__(self, web_driver, url = ''):
        self._web_driver = web_driver
        self.get(url)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self.__getattribute__(name).set_value(self._web_driver, value)
        else :
            super(WebPage, self).__setattr__(name, value)

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if not item.startswith('_') and not callable(attr):
        attr._web_driver = self._web_driver
        attr._page = self

        return attr


def get(self,url):
    self._web_driver.get(url)

def go_back(self):
    self._web_driver()
    self.wait_page_loaded()

def refresh(self):
    self._web_driver.refresh()
    self.wait_page_loaded()


def screenshot(self, file_name = 'screenshot.png'):

    self._web_driver.save_screenshot(file_name)
    self._web_driver.get(url)

def go_back(self):
    self._web_driver.back()


    if not item.startswith('_') and not callable(attr):
        attr.web_driver
        attr = object.__getattribute__(self, item)