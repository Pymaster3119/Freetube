from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)

username = input("What is your username?")
password = input("What is your password?")

driver.get("https://www.youtube.com")

#Click signin
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer")))
driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer").click()
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

#Send username
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(username)
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]")))
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]").click()
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

#Send password
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")))
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]")))
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]").click()
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

input()