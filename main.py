import sys
import time
from creds import GitHub
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/")
driver.maximize_window()

# Logging into GitHub
login_btn = driver.find_element(by='xpath', value='/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
login_btn.click()

username_field = driver.find_element(by='xpath', value='//*[@id="login_field"]')
username_field.send_keys(GitHub.USERNAME)
password_field = driver.find_element(by='xpath', value='//*[@id="password"]')
password_field.send_keys(GitHub.PASSWORD)
signIn_btn = driver.find_element(by='xpath', value='//*[@id="login"]/div[4]/form/div/input[12]')
signIn_btn.click()

# Creating a repository
driver.get("https://github.com/new")
repo_name = sys.argv[1]

repoName_field = driver.find_element(by='xpath', value='//*[@id="repository_name"]')
repoName_field.click()
repoName_field.send_keys(repo_name)
time.sleep(1)
create_btn = driver.find_element(by='xpath', value='//*[@id="new_repository"]/div[5]/button')
create_btn.click()

# Closing the browser
driver.quit()