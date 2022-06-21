from selenium import webdriver
from creds import GitHub

driver = webdriver.Chrome()
driver.get("https://github.com/")
driver.maximize_window()

login_btn = driver.find_element(by='xpath', value='/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
login_btn.click()

username_field = driver.find_element(by='xpath', value='//*[@id="login_field"]')
username_field.send_keys(GitHub.USERNAME)
password_field = driver.find_element(by='xpath', value='//*[@id="password"]')
password_field.send_keys(GitHub.PASSWORD)
signIn_btn = driver.find_element(by='xpath', value='//*[@id="login"]/div[4]/form/div/input[12]')
signIn_btn.click()