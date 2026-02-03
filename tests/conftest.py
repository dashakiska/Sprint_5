import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from src.data import main_site
from src.data import Credentials
from src.locators import Locators

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    browser = webdriver.Chrome(options)
    browser.get(main_site)
    yield browser
    browser.quit()
