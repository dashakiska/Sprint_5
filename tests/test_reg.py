from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site
import random



class TestRegistrationWithNewCredantials:
    def test_success_registration(self, driver):
        
        driver.find_element(*Locators.LOG_TO_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys("Darya")
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(f"daria{random.randint(100, 999)}@yy.yu")
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver,30).until(EC.url_contains("/login"))
        assert driver.current_url == main_site + 'login'
        driver.quit()


    def test_short_password_fail(self, driver):

        driver.find_element(*Locators.LOG_TO_ACC_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys("Darya")
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.EMAIL))
        driver.find_element(*Locators.EMAIL).send_keys(f"daria{random.randint(100, 999)}@yy.yu")
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.PASSWORD))
        driver.find_element(*Locators.PASSWORD).send_keys("123")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Некорректный пароль']")))
        error = driver.find_element(By.XPATH, "//*[contains(text(), 'Некорректный пароль')]").text
        assert error == "Некорректный пароль" 
        driver.quit()   

        
        
        
        
