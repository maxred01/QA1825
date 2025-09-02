import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://demoqa.com/webtables"

@pytest.fixture(scope="session")
def driver():
     options = Options()
     options.add_argument("--start-maximized")

     driver = webdriver.Chrome(options=options)
     driver.get(URL)

     yield driver

     driver.quit()
