from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print("Type in your email  password")
username = input(">> ")
password = input(">> ")
tweet = "hello world"

# LOGIN
url = "https://twitter.com/i/flow/login"
driver = webdriver.Chrome("chromedriver")
driver.get(url)
time.sleep(35)

# USERNAME
username_field = driver.find_element(By.CLASS_NAME, "r-homxoj")
username_field.send_keys(username)
time.sleep(3)
username_field.send_keys(Keys.RETURN)
time.sleep(10)

# PASSWORD
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
time.sleep(3)
tweets_field = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block public-DraftStyleDefault-ltr")
tweets_field.send_keys(tweet)
time.sleep(60)



print('Script Succesfull')
