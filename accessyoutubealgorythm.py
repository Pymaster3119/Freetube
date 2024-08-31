from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

chrome_path = "=/Users/aditya/Desktop/InProgress/Freetube 2.0/ChromeStandaloneSetup64.exe"

service = Service(executable_path=os.path.abspath("/Users/aditya/Desktop/InProgress/Freetube 2.0/chromedriver 2"))
options = Options()
options.binary_location = chrome_path

driver = webdriver.Chrome(service=service, options=options)