from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print("Type in your email  password")
username = input(">> ")
password = input(">> ")


# LOGIN
url = "https://twitter.com/i/flow/login"
driver = webdriver.Chrome("chromedriver")
driver.get(url)
time.sleep(35)



# USERNAME
username_field = driver.find_element(By.CLASS_NAME, "r-homxoj")
username_field.send_keys(username)
username_field.send_keys(Keys.RETURN)
time.sleep(10)

# PASSWORD
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(200)

# TWEET
tweets_field = driver.find_element(By.CLASS_NAME, "r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ceczpf r-1ny4l3l r-t60dpp r-1ttztb7")
tweets_field.send_keys("Eyin fans mi")
tweet_button =  driver.find_element(By.CSS_SELECTOR, "tweetButtonInline").click



time.sleep(120)

print('Script Succesfull')
