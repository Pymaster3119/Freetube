from selenium import webdriver
from selenium.webdriver.firefox.service import Service;
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support import expected_conditions as EC
import os
import time

options = Options()
options.set_preference("profile", "/Users/aditya/Desktop/DisabledDriver/o0fvibos.Adblock Profile")
driver = webdriver.Firefox(options=options, service=Service(executable_path = os.path.realpath("geckodriver")))
driver.set_window_size(1000,1000)

username = input("What is your google username?")
password = input("What is your password?")

driver.get("https://www.youtube.com")
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(username)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]').click()