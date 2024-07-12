from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

def first_move(driver):
    # Taking 0-3 and 5-8 on each side with 4 left out. The lighter side will have the fake brick
    driver.find_element(by=By.ID, value="left_0").send_keys("0")
    driver.find_element(by=By.ID, value="left_1").send_keys("1")
    driver.find_element(by=By.ID, value="left_2").send_keys("2")
    driver.find_element(by=By.ID, value="left_3").send_keys("3")
    driver.find_element(by=By.ID, value="right_0").send_keys("5")
    driver.find_element(by=By.ID, value="right_1").send_keys("6")
    driver.find_element(by=By.ID, value="right_2").send_keys("7")
    driver.find_element(by=By.ID, value="right_3").send_keys("8")
    driver.find_element(by=By.ID, value="weigh").click()

def is_hole_in_one(driver):
    # There is a possibility that the brick i left out is the lighter one, this is that check
    time.sleep(5)        
    last_li = driver.find_element(By.XPATH, "//li[last()]").text
    if '=' in last_li:
        driver.find_element(by=By.ID, value="coin_4").click()   

def return_lighter_set(driver):
    # this returns the array of the numbers of the lighter bricks
    last_li = driver.find_element(By.XPATH, "//li[last()]").text
    if ">" in last_li:
        split = last_li.split(">")
        possible = json.loads(split[1])
    elif "<" in last_li:
        split = last_li.split("<")
        possible = json.loads(split[0])        
    driver.find_element(by=By.CSS_SELECTOR, value="div:nth-child(4) > #reset").click()
    return possible

def second_move(driver, possible):
    # Again I am spliting to find the lighter side
    driver.find_element(by=By.ID, value="left_0").send_keys(possible[0])
    driver.find_element(by=By.ID, value="left_1").send_keys(possible[1])
    driver.find_element(by=By.ID, value="right_0").send_keys(possible[2])
    driver.find_element(by=By.ID, value="right_1").send_keys(possible[3])
    driver.find_element(by=By.ID, value="weigh").click()
    time.sleep(5)

def third_move(driver, possible):
    # Finally this will return one number of the brick that is lighter
    driver.find_element(by=By.ID, value="left_0").send_keys(possible[0])
    driver.find_element(by=By.ID, value="right_0").send_keys(possible[1])
    driver.find_element(by=By.ID, value="weigh").click()
    time.sleep(5)

