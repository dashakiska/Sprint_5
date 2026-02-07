from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.data import Credentials
from src.locators import Locators
from src.data import main_site

class TestKit:
        
        def test_go_to_buns_section(self, driver):
            driver.find_element(*Locators.SAUCE_TAB).click()
            driver.find_element(*Locators.BUNS_TAB).click()
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(Locators.BUNS_TAB,"class",Locators.KIT_TAB))
            assert Locators.KIT_TAB in driver.find_element(*Locators.BUNS_TAB).get_attribute("class")
            


        def test_go_to_sauce_section(self, driver):
            driver.find_element(*Locators.FILLING_TAB).click()
            driver.find_element(*Locators.SAUCE_TAB).click()
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(Locators.SAUCE_TAB,"class",Locators.KIT_TAB))
            assert Locators.KIT_TAB in driver.find_element(*Locators.SAUCE_TAB).get_attribute("class")
            


        def test_go_to_filling_section(self, driver):
            driver.find_element(*Locators.SAUCE_TAB).click()
            driver.find_element(*Locators.FILLING_TAB).click()
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(Locators.FILLING_TAB,"class",Locators.KIT_TAB))
            assert Locators.KIT_TAB in driver.find_element(*Locators.FILLING_TAB).get_attribute("class")
                               