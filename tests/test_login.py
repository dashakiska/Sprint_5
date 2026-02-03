from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site

class TestLogin:
        
        def test_login_button_on_main_site(self, driver):
            driver.find_element(*Locators.LOG_TO_ACC_BUTTON).click()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
            driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
            WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
            driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
            driver.find_element(*Locators.ENTER_BUTTON).click()
            WebDriverWait(driver,10).until(EC.url_contains(main_site))
            assert main_site in driver.current_url 
            driver.quit()
            

        def test_login_button_account(self, driver):
             driver.find_element(*Locators.ACCOUNT_BUTTON).click()
             WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
             driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
             WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
             driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
             driver.find_element(*Locators.ENTER_BUTTON).click()
             WebDriverWait(driver,10).until(EC.url_contains(main_site))
             assert main_site in driver.current_url 
             driver.quit()

        def test_login_Reg_form_button(self, driver):
             driver.find_element(*Locators.ACCOUNT_BUTTON).click()
             driver.find_element(*Locators.REG_BUTTON).click()
             driver.find_element(*Locators.ENTER_BUTTON).click()
             WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
             driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
             WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
             driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
             driver.find_element(*Locators.ENTER_BUTTON).click()
             WebDriverWait(driver,10).until(EC.url_contains(main_site))
             assert main_site in driver.current_url 
             driver.quit()   

        def test_login_recover_password_button(self, driver):
             driver.find_element(*Locators.ACCOUNT_BUTTON).click()
             driver.find_element(*Locators.RECOVER_PASSWORD).click()
             driver.find_element(*Locators.ENTER_BUTTON).click()
             WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
             driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
             WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
             driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
             driver.find_element(*Locators.ENTER_BUTTON).click()
             WebDriverWait(driver,10).until(EC.url_contains(main_site))
             assert main_site in driver.current_url 
             driver.quit()                       