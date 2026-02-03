from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site

class TestKit:
        
        def test_go_to_buns_section(self, driver):
            active_section = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_BUNS))
            assert active_section.text == 'Булки'
            driver.quit()


        def test_go_to_sauce_section(self, driver):
            driver.find_element(*Locators.SAUCE_BUTTON).click()
            element = driver.find_element(*Locators.TEXT_SAUCE)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            assert element.text == 'Соусы'
            driver.quit()


        def test_go_to_filling_section(self, driver):
            driver.find_element(*Locators.FILLING_BUTTON).click()
            element = driver.find_element(*Locators.TEXT_FILLING)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            assert element.text == 'Начинки'
            driver.quit()                   