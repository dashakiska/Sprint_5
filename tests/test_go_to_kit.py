from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site

class TestGoToKit:
        
        def test_go_to_kit_from_account(self, driver):
            driver.find_element(*Locators.LOG_TO_ACC_BUTTON).click()
            driver.find_element(*Locators.KIT_BUTTON).click()
            WebDriverWait(driver,10).until(EC.url_contains(main_site))
            assert main_site in driver.current_url 
            driver.quit()
