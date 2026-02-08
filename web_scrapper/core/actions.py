from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import EXPLICIT_WAIT
import exceptions

class Actions:
    def __init__(self, driver):
        self.driver = driver

    def click(self, xpath, timeout=EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()

    def write(self, xpath, text, timeout=EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.clear()
        element.send_keys(text)


    def select(self, xpath, value, timeout=EXPLICIT_WAIT):
        
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            element = Select(element)
            element.select_by_value(value)
        except NoSuchElementException:
            raise exceptions.BusinessException("No option in the dropdown list.")


    def read(self, xpath, timeout=EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element.text
    
    def if_exist(self, xpath, timeout=EXPLICIT_WAIT):
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False
        
