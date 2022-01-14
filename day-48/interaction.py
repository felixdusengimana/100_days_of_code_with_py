from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

google_web_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=google_web_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, "fName")
lName = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
btn = driver.find_element(By.CSS_SELECTOR, "form button")

fName.send_keys("Felix")
lName.send_keys("Dusengimana")
email.send_keys("phelixdusenge@gmail.com")
btn.click()



