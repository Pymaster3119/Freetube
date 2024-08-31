from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options)

username = input("What is your username?")
password = input("What is your password?")

driver.get("https://www.youtube.com")
actions = ActionChains(driver)

#Click signin
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer")))
driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer").click()
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

#Send username
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
actions.move_by_offset(776, 842).click().perform()
actions.send_keys(username).perform()
actions.move_by_offset(-776, -842).perform()
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]")))
print(driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]").location)
actions.move_by_offset(737, 816).click().perform()
actions.move_by_offset(-737, -816).perform()
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

#Send password
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")))
actions.move_by_offset(776, 842).click().perform()
actions.send_keys(password).perform()
actions.move_by_offset(-776, -842).perform()
WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]")))
actions.move_by_offset(737, 816).click().perform()
actions.move_by_offset(-737, -816).perform()
WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

#Skip past security (if applicable)
try:
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div/div/button/div[3]")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]/div/div/button/div[3]").click()
    WebDriverWait(driver, 1000).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
except:
    print('No security found')


def find_recommendations():
    pass

if __name__ == "__main__":
    find_recommendations()

input()