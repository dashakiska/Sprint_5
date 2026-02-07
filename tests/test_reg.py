from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site
import random
from src.data import Endpoints



class TestRegistrationWithNewCredantials:
    def test_success_registration(self, driver):
        
        driver.find_element(*Locators.LOG_TO_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.rand_email)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.url_contains(Endpoints.LOGIN))
        


    def test_short_password_fail(self, driver):

        driver.find_element(*Locators.LOG_TO_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.rand_email)
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.short_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
         

        
        
        
        
