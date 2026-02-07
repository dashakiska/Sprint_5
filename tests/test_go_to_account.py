from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site
from src.data import Endpoints

class TestGoToAccount:
        
        def test_go_to_account_from_main_site(self, driver):
            driver.find_element(*Locators.ACCOUNT_BUTTON).click()
            assert WebDriverWait(driver, 10).until(EC.url_contains(Endpoints.LOGIN))
        
                        