from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://www.python.org")
times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
link_text = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

events_created = {}
for i in range(len(times)):
    events_created[i] = {
        "time": times[i].text,
        "event": link_text[i].text
    }

print(events_created)

driver.quit()
