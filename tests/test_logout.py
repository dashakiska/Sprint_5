from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site

class TestLogout:
        
        def test_logout_button(self, driver):
            driver.find_element(*Locators.ACCOUNT_BUTTON).click()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
            driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
            WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
            driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
            driver.find_element(*Locators.ENTER_BUTTON).click()
            WebDriverWait(driver,10).until(EC.url_contains(main_site))
            WebDriverWait(driver,10).until(EC.invisibility_of_element_located(Locators.MODAL_OVERLAY))
            account_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located(Locators.ACCOUNT_BUTTON))
            driver.execute_script("arguments[0].click();", account_btn)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
            driver.find_element(*Locators.LOGOUT_BUTTON).click()
            WebDriverWait(driver,30).until(EC.url_contains("/login"))
            assert driver.current_url == main_site + 'login'
            driver.quit()