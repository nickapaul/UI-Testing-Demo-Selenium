import Helpers.help as help
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestSDET():    
    def test_case1(self):
        # Arrange
        possible = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        driver = webdriver.Edge()
        driver.get("http://sdetchallenge.fetch.com/")

        # First Check
        help.first_move(driver)
        help.is_hole_in_one(driver)        
        possible = help.return_lighter_set(driver)

        # Second Check
        help.second_move(driver, possible)
        possible = help.return_lighter_set(driver)

        # Third Check
        help.third_move(driver, possible)
        possible = help.return_lighter_set(driver)

        # Assert
        driver.find_element(by=By.ID, value=f"coin_{possible[0]}").click()
        n=1
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(), 'Timed out waiting for alert to appear.')
            alert = driver.switch_to.alert
            assert alert.text == 'Yay! You find it!'
        except TimeoutException:
            print("No alert")