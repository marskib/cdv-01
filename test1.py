from selenium import webdriver
from time import sleep

driver = webdriver.Firefox();
driver.get("https://cdv.pl")
sleep(2)
driver.quit()